from utils.operators import get_datatype


class GenerateSourceString:
    def __init__(self, data: dict):
        self.__data = data
        self.__import_str = ""
        self.__arg_str = ""
        self.__global_str = ""
        self.__relation_str = ""
        self.__dag_str = ""

    # TODO: Render arguments based on the datatype. Example: If the argument is integer render it without quotes
    def __generate_operator_statements(self, operators: dict, dag_variable_name: str) -> list:
        args = {}
        for operator in list(set([operators[key]["name"] for key in operators])):
            args[operator] = get_datatype(operator)

        for key in operators:
            operator = operators[key]
            operator_args_str = f"""{operator['name']}("""
            for k, v in operator["args"].items():
                if v != "":
                    # finding the datatype for the particular argument. If integer render without quotes
                    # TODO: Currenly quote removal is added only for integer values. For other datatypes quotes are default. Need to test on other datatypes and update accordingly
                    arg_type = (
                        args[f'{operator["name"]}'].get(f"{k}", None)["data_type"]
                        if args[f'{operator["name"]}'].get(f"{k}", None) != None
                        else "string"
                    )
                    operator_args_str += (
                        f"""{k} = {v},"""
                        # if k == "python_callable"
                        if k == "python_callable" or arg_type == "int"
                        else f"""{k} = '{v}',"""
                    )
            operator_args_str += f"""dag = {dag_variable_name})\n"""
            self.__arg_str += f'{operator["args"]["task_id"]} = {operator_args_str}'

    def __generate_global_string(self, data: str) -> None:
        if data != "":
            self.__global_str += f"""{data}
"""

    def __generate_import_statements(self, data: str) -> None:
        if data != "":
            self.__import_str += f"""{data}
"""

    def __generate_dag_statement(self, data: str) -> None:
        if data != "":
            self.__dag_str += f"""{data["dag_variable_name"]} = {data["call"]}
"""

    def __get_relation(self, root_node, edges, relation):
        for edge in edges:
            if edge["source"] == root_node:
                relation[edge["target"]] = {}
                self.__get_relation(edge["target"], edges, relation[edge["target"]])

    def __convert_relation_to_string(self, input_dict, output_list=None, parent_keys=None):
        if output_list is None:
            output_list = []
        if parent_keys is None:
            parent_keys = []
        for key, value in input_dict.items():
            # current_keys = parent_keys + [key]
            # Adding task_id instead of key to match with the UI
            current_keys = parent_keys + [self.__data["operators"][key]["args"]["task_id"]]
            if isinstance(value, dict) and value:
                self.__convert_relation_to_string(value, output_list=output_list, parent_keys=current_keys)
            elif isinstance(value, dict) and not value:
                output_list.append(" >> ".join(current_keys))
        return "\n".join(output_list)

    def __generate_relation_graph_string(self, edges: list, operators: dict) -> str:
        sources = set()
        targets = set()
        for edge in edges:
            sources.add(edge["source"])
            targets.add(edge["target"])
        roots = list(sources - targets)

        # orphans - With no source and target
        orphans = list(set(operators.keys()) - set(list(sources) + list(targets)))

        relation = {}
        for root in roots:
            relation[root] = {}
            self.__get_relation(root, edges, relation[root])

        # Adding task_id instead of key for the orphans to match with the UI
        orphans = "\n".join([self.__data["operators"][x]["args"]["task_id"] for x in orphans])
        self.__relation_str = self.__convert_relation_to_string(relation) + f"\n{orphans}"

    def get(self) -> str:
        # Calling the functions to generate the source code string
        self.__generate_import_statements(self.__data["import_statements"])
        self.__generate_dag_statement(self.__data["dag_statement"])
        self.__generate_operator_statements(self.__data["operators"], self.__data["dag_statement"]["dag_variable_name"])
        self.__generate_global_string(self.__data["global_statements"])
        self.__generate_relation_graph_string(
            self.__data["react_flow_data"]["edges"], operators=self.__data["operators"]
        )
        return self.__import_str + self.__dag_str + self.__global_str + self.__arg_str + self.__relation_str
