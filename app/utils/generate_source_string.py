class GenerateSourceString:
    import_str = set()
    arg_str = ""
    global_str = ""

    @staticmethod
    def __generate_import_and_operator_statements(operators: dict) -> list:
        # Variable to store import statements
        import_str = set()
        # Variable to store operator statements
        arg_str = ""
        for key in operators:
            operator = operators[key]
            import_str.add(f"""from {operator['import_path']} import {operator['name']}
""")
            # Variable to store operator arguments
            operator_args_str = f"""{operator['name']}("""
            for k, v in operator["args"].items():
                if (v != ""):
                    operator_args_str += f"""{k} = {v},""" if k == "python_callable" else f"""{k} = '{v}',"""
            operator_args_str += f"""dag = dag)\n"""
            arg_str += f'{key} = {operator_args_str}'

        return "".join(list(import_str)), arg_str

    @staticmethod
    def __generate_global_string(data: str) -> str:
        global_str = ""
        if (data != ""):
            global_str += f"""{data}
"""
        return global_str

    def get(data: dict) -> str:
        import_str, arg_str = GenerateSourceString.__generate_import_and_operator_statements(data["operators"])
        global_str = GenerateSourceString.__generate_global_string(data["global"])
        return import_str + global_str + arg_str
