import inspect

ALLOWED_OPERATORS = {
    "PythonOperator": (1, "airflow.operators.python"),
    "BashOperator": (2, "airflow.operators.bash"),
}


def import_from(filename, functionName):
    module = __import__(filename, fromlist=[functionName])
    return getattr(module, functionName)


def get_datatype(operator_name: str) -> dict:
    imported_operator = import_from(
        ALLOWED_OPERATORS[operator_name][1],
        operator_name,
    )
    return get_default_args(imported_operator.__init__)


def get_default_args(func) -> dict:
    # To get if an argument is mandatory to create an object in Python, you can check if the argument has a default value of inspect.Parameter.empty. If it does not have a default value, then the argument is mandatory.
    sig = inspect.signature(func)
    res = {}
    for param in sig.parameters.values():
        if param.name in ["self", "args", "kwargs"]:
            continue
        temp = {}
        if param.default is not inspect.Parameter.empty:
            datatype = "" if type(param.default).__name__ == "NoneType" else type(param.default).__name__
            if datatype == "int":
                __default_argument = int(param.default)
            elif datatype == "None" or datatype == "":
                __default_argument = ""
            else:
                print(datatype)
                __default_argument = str(param.default)
            temp["default_argument"] = __default_argument
            temp["data_type"] = datatype
            temp["required"] = False
        else:
            temp["default_argument"] = ""
            temp["data_type"] = ""
            temp["required"] = True
        res[param.name] = temp
    return res


def get_operators() -> dict:
    operators = []
    for operator in ALLOWED_OPERATORS:
        operator_details = {}
        imported_operator = import_from(
            ALLOWED_OPERATORS[operator][1],
            operator,
        )
        operator_info = get_default_args(imported_operator.__init__)
        operator_info["task_id"] = {"default_argument": "", "data_type": "string", "required": True}
        operator_details["args"] = operator_info
        operator_details["name"] = operator
        operator_details["node_type"] = "operator"
        operator_details["id"] = ALLOWED_OPERATORS[operator][0]
        operator_details["import_path"] = ALLOWED_OPERATORS[operator][1]
        operators.append(operator_details)

    return operators
