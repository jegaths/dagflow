import json
from utils.json_to_source import JsonToSource
from utils.operators import get_operator_details
from utils.model.pipeline_model import Pipeline
import uuid

uid = uuid.uuid4()


class DagToDagFlow:
    def __init__(self, json_string: str = None, file_path: str = None) -> None:
        if file_path == None and json_string == None:
            print("Filepath or json string should be given!")
            return
        if json_string == None:
            with open(file_path, "r") as f:
                self.__json_data = json.load(f)
        else:
            self.__json_data = json.loads(json_string)
        self.empty_ast = {"_type": "Module", "body": [], "type_ignores": []}
        self.seperated_statements = {}
        self.__import_statements = ""
        self.__global_statements = ""
        self.__nodes = []
        self.__operators = {}
        self.__edges = []
        self.__dag_statement = ""

    # Seperate json into different statements
    def __seperate_source_json(self, data):
        import_statements = []
        dag_statment = None
        global_statments = []
        operator_statments = []
        binop_statements = []
        variable_taskId_mapping = {}
        operator_vars = set()
        for item in data["body"]:
            if item["_type"] == "ImportFrom" or item["_type"] == "Import":
                import_statements.append(item)
            elif (
                item["_type"] == "Assign" and item["value"]["_type"] == "Call" and item["value"]["func"]["id"] == "DAG"
            ):
                dag_statment = item
            elif item["_type"] == "FunctionDef":
                global_statments.append(item)
            # !Operator _type can be Assign or Expr. Assuming we can distinguish between operator and other statements by checking the arguments. Operators will have task_id and dag as arguments.
            # !If we have Binop Expr then we have to add edges
            elif (item["_type"] == "Expr" and item["value"]["_type"] == "Call") or (
                item["_type"] == "Assign" and item["value"]["_type"] == "Call"
            ):
                keywords = item["value"].get("keywords", [])
                keywords = [x for x in keywords if x["arg"] == "task_id" or x["arg"] == "dag"]
                if len(keywords) == 2:
                    if item["_type"] == "Assign":
                        operator_vars.add(item["targets"][0]["id"])
                        variable_taskId_mapping[item["targets"][0]["id"]] = [
                            x["value"]["value"] for x in keywords if x["arg"] == "task_id"
                        ][0]
                    operator_statments.append(item)
            elif item["value"]["_type"] == "BinOp":
                binop_statements.append(item)
            else:
                # skip adding to global assignment if it is a operator expression. Eg: mytaskvariableName
                if item["_type"] == "Expr" and item.get("value", {}).get("id", "") in operator_vars:
                    continue
                global_statments.append(item)
        self.seperated_statements = {
            "import_statements": import_statements,
            "dag_statment": dag_statment,
            "global_statments": global_statments,
            "operator_statments": operator_statments,
            "binop_statements": binop_statements,
            "variable_taskId_mapping": variable_taskId_mapping,
        }

    def __extract_edge_source_target_pairs(self, expr):
        pairs = []
        if expr["_type"] == "BinOp":
            if expr["left"]["_type"] == "Name" and expr["right"]["_type"] == "Name":
                pairs.append(
                    {
                        "animated": True,
                        "id": f'reactflow__edge-{self.seperated_statements["variable_taskId_mapping"][expr["left"]["id"]]}a-{self.seperated_statements["variable_taskId_mapping"][expr["right"]["id"]]}a',
                        "sourceHandle": "a",
                        "targetHandle": "a",
                        "source": expr["left"]["id"],
                        "target": expr["right"]["id"],
                    }
                )
            elif expr["left"]["_type"] == "BinOp" and expr["right"]["_type"] == "Name":
                pairs += self.__extract_edge_source_target_pairs(expr["left"])
                pairs.append(
                    {
                        "animated": True,
                        "id": f'reactflow__edge-{self.seperated_statements["variable_taskId_mapping"][expr["left"]["right"]["id"]]}a-{self.seperated_statements["variable_taskId_mapping"][expr["right"]["id"]]}a',
                        "sourceHandle": "a",
                        "targetHandle": "a",
                        "source": expr["left"]["right"]["id"],
                        "target": expr["right"]["id"],
                    }
                )
            elif expr["left"]["_type"] == "Name" and expr["right"]["_type"] == "BinOp":
                pairs.append(
                    {
                        "animated": True,
                        "id": f'reactflow__edge-{self.seperated_statements["variable_taskId_mapping"][expr["left"]["id"]]}a-{self.seperated_statements["variable_taskId_mapping"][expr["right"]["left"]["id"]]}a',
                        "sourceHandle": "a",
                        "targetHandle": "a",
                        "source": expr["left"]["id"],
                        "target": expr["right"]["left"]["id"],
                    }
                )
                pairs += self.__extract_edge_source_target_pairs(expr["right"])
            elif expr["left"]["_type"] == "BinOp" and expr["right"]["_type"] == "BinOp":
                pairs += self.__extract_edge_source_target_pairs(expr["left"])
                pairs += self.__extract_edge_source_target_pairs(expr["right"])
                pairs.append(
                    {
                        "animated": True,
                        "id": f'reactflow__edge-{self.seperated_statements["variable_taskId_mapping"][expr["left"]["right"]["id"]]}a-{self.seperated_statements["variable_taskId_mapping"][expr["right"]["left"]["id"]]}a',
                        "sourceHandle": "a",
                        "targetHandle": "a",
                        "source": expr["left"]["right"]["id"],
                        "target": expr["right"]["left"]["id"],
                    }
                )
        return pairs

    def __generate_import_staments(self, statements: list):
        self.empty_ast["body"] = []
        self.empty_ast["body"].extend(statements)
        self.__import_statements = JsonToSource(json_string=json.dumps(self.empty_ast)).get()

    def __generate_global_staments(self, statements: list):
        self.empty_ast["body"] = []
        self.empty_ast["body"].extend(statements)
        self.__global_statements = JsonToSource(json_string=json.dumps(self.empty_ast)).get()

    def __generate_dag_statement(self, statements: list):
        self.empty_ast["body"] = []
        self.empty_ast["body"].append(statements["value"])
        # self.__dag_statement = JsonToSource(json_string=json.dumps(self.empty_ast)).get()
        self.__dag_statement = {
            "dag_variable_name": statements["targets"][0]["id"],
            "call": JsonToSource(json_string=json.dumps(self.empty_ast)).get(),
        }

    async def __generate_nodes_and_operators(self, statements: list):
        operators_details = {}

        def __generate_args(keywords, all_args):
            args = {}
            existin_args = [arg["arg"] for arg in keywords if arg["arg"] != "dag"]
            for arg in all_args:
                if arg not in existin_args:
                    args[arg] = all_args[arg]["default_argument"]
                else:
                    args[arg] = (
                        keywords[existin_args.index(arg)]["value"]["id"]
                        if keywords[existin_args.index(arg)]["value"]["_type"] == "Name"
                        else keywords[existin_args.index(arg)]["value"]["value"]
                    )
            return args

        posx = 0
        width = 264
        for item in statements:
            self.__nodes.append(
                {
                    "width": 264,
                    "height": 86,
                    "id": item["targets"][0]["id"],
                    "type": "operator",
                    "position": {"x": posx, "y": 0},
                    "data": item["targets"][0]["id"],
                    "selected": False,
                    "positionAbsolute": {"x": posx, "y": 0},
                    "dragging": False,
                }
            )
            posx += width + 20

            # operator_details
            operator_name = item["value"]["func"]["id"]
            if operator_name not in operators_details:
                operator = await get_operator_details(operator_name=operator_name, projection={"args": 1, "import_path": 1})
                operators_details[operator_name] = operator

            self.__operators[item["targets"][0]["id"]] = {
                "name": item["value"]["func"]["id"],
                "import_path": operators_details[operator_name]["import_path"],
                "args": __generate_args(item["value"]["keywords"], operators_details[operator_name]["args"]),
                "description": "",
            }

    async def generate_dagflow(self) -> Pipeline:
        self.__seperate_source_json(self.__json_data)
        for binop_statement in self.seperated_statements["binop_statements"]:
            self.__edges.extend(self.__extract_edge_source_target_pairs(binop_statement["value"]))
        self.__edges = list(set(tuple(sorted(d.items())) for d in self.__edges))
        self.__edges = [dict(t) for t in self.__edges]

        self.__generate_dag_statement(self.seperated_statements["dag_statment"])
        self.__generate_import_staments(self.seperated_statements["import_statements"])
        self.__generate_global_staments(self.seperated_statements["global_statments"])
        await self.__generate_nodes_and_operators(self.seperated_statements["operator_statments"])

        res = {
            "pipeline_name": "",
            "pipeline_id": str(uid),
            "global_statements": self.__global_statements,
            "operators": self.__operators,
            "react_flow_data": {
                "nodes": self.__nodes,
                "edges": self.__edges,
                "viewport": {"x": 0, "y": 0, "zoom": 1},
            },
            "import_statements": self.__import_statements,
            "dag_statement": self.__dag_statement,
        }

        return Pipeline(**{"data": res})
