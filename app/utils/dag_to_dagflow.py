import json
from utils.json_to_source import JsonToSource


class DagToDagFlow:
    def __init__(self, json_string: str = None, file_path: str = None) -> None:
        if (file_path == None and json_string == None):
            print("Filepath or json string should be given!")
            return
        if (json_string == None):
            with open(file_path, "r") as f:
                json_data = json.load(f)
        else:
            json_data = json.loads(json_string)
        self.empty_ast = {
            "_type": "Module",
            "body": [],
            "type_ignores": []
        }
        self.seperated_statements = {}
        self.__generate_dagflow(json_data)

    def __seperate_source_json(self, data):  # Seperate json into different statements
        import_statements = []
        dag_statment = None
        global_statments = []
        operator_statments = []
        binop_statements = []
        variable_taskId_mapping = {}
        for item in data["body"]:
            if (item["_type"] == "ImportFrom" or item["_type"] == "Import"):
                import_statements.append(item)
            elif (item["_type"] == "Assign" and item["value"]["_type"] == "Call" and item["value"]["func"]["id"] == "DAG"):
                dag_statment = item
            elif (item["_type"] == "FunctionDef"):
                global_statments.append(item)
            # !Operator _type can be Assign or Expr. Assuming we can distinguish between operator and other statements by checking the arguments. Operators will have task_id and dag as arguments.
            # !If we have Binop Expr then we have to add edges
            elif ((item["_type"] == "Expr" and item["value"]["_type"] == "Call") or (item["_type"] == "Assign" and item["value"]["_type"] == "Call")):
                keywords = item["value"].get("keywords", [])
                keywords = [x for x in keywords if x["arg"] == "task_id" or x["arg"] == "dag"]
                if len(keywords) == 2:
                    if (item["_type"] == "Assign"):
                        variable_taskId_mapping[item["targets"][0]["id"]] = [x["value"]["value"] for x in keywords if x["arg"] == "task_id"][0]
                    operator_statments.append(item)
            elif (item["value"]["_type"] == "BinOp"):
                binop_statements.append(item)
            else:
                global_statments.append(item)
        self.seperated_statements = {"import_statements": import_statements, "dag_statment": dag_statment, "global_statments": global_statments,
                                     "operator_statments": operator_statments, "binop_statements": binop_statements, "variable_taskId_mapping": variable_taskId_mapping}

    def __extract_edge_source_target_pairs(self, expr):
        pairs = []
        if expr['_type'] == 'BinOp':
            if expr['left']['_type'] == 'Name' and expr['right']['_type'] == 'Name':
                pairs.append({
                    'animated': True,
                    'id': f'reactflow__edge-{self.seperated_statements["variable_taskId_mapping"][expr["left"]["id"]]}a-{self.seperated_statements["variable_taskId_mapping"][expr["right"]["id"]]}a',
                    'sourceHandle': 'a',
                    'targetHandle': 'a',
                    'source': expr['left']['id'],
                    'target': expr['right']['id']
                })
            elif expr['left']['_type'] == 'BinOp' and expr['right']['_type'] == 'Name':
                pairs += self.__extract_edge_source_target_pairs(expr['left'])
                pairs.append({
                    'animated': True,
                    'id': f'reactflow__edge-{self.seperated_statements["variable_taskId_mapping"][expr["left"]["right"]["id"]]}a-{self.seperated_statements["variable_taskId_mapping"][expr["right"]["id"]]}a',
                    'sourceHandle': 'a',
                    'targetHandle': 'a',
                    'source': expr['left']['right']['id'],
                    'target': expr['right']['id']
                })
            elif expr['left']['_type'] == 'Name' and expr['right']['_type'] == 'BinOp':
                pairs.append({
                    'animated': True,
                    'id': f'reactflow__edge-{self.seperated_statements["variable_taskId_mapping"][expr["left"]["id"]]}a-{self.seperated_statements["variable_taskId_mapping"][expr["right"]["left"]["id"]]}a',
                    'sourceHandle': 'a',
                    'targetHandle': 'a',
                    'source': expr['left']['id'],
                    'target': expr['right']['left']['id']
                })
                pairs += self.__extract_edge_source_target_pairs(expr['right'])
            elif expr['left']['_type'] == 'BinOp' and expr['right']['_type'] == 'BinOp':
                pairs += self.__extract_edge_source_target_pairs(expr['left'])
                pairs += self.__extract_edge_source_target_pairs(expr['right'])
                pairs.append({
                    'animated': True,
                    'id': f'reactflow__edge-{self.seperated_statements["variable_taskId_mapping"][expr["left"]["right"]["id"]]}a-{self.seperated_statements["variable_taskId_mapping"][expr["right"]["left"]["id"]]}a',
                    'sourceHandle': 'a',
                    'targetHandle': 'a',
                    'source': expr['left']['right']['id'],
                    'target': expr['right']['left']['id']
                })
        return pairs

    def __generate_import_staments(self, imports: list):
        self.empty_ast["body"] = []
        self.empty_ast["body"].extend(imports)
        print(JsonToSource(json_string=json.dumps(self.empty_ast)).get())

    def __generate_dagflow(self, data):
        self.__seperate_source_json(data)
        edges = []
        for binop_statement in self.seperated_statements["binop_statements"]:
            edges.extend(self.__extract_edge_source_target_pairs(binop_statement["value"]))

        self.__generate_import_staments(self.seperated_statements["import_statements"])
        print(json.dumps(edges, indent=4))
