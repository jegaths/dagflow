import inspect

ALLOWED_OPERATORS = {
    "PythonOperator": (1, "airflow.operators.python"),
    "BashOperator": (2, "airflow.operators.bash"),
}


def import_from(filename, functionName):
    module = __import__(filename, fromlist=[functionName])
    return getattr(module, functionName)


def get_default_args(func) -> dict:
    signature = inspect.signature(func)
    return {
        k: {
            "default_argument": str(v.default)
            if v.default is not inspect.Parameter.empty and v.default != None
            else "",
            "data_type": str(v.annotation) if v.annotation is not inspect.Parameter.empty else "No datatype specified",
        }
        for k, v in signature.parameters.items()
        if k not in ["self"]
    }


def get_default_args_v2(func) -> dict:
    sig = inspect.signature(func)
    res = {}
    for param in sig.parameters.values():
        if param.name in ["self", "args", "kwargs"]:
            continue
        temp = {}
        if param.default is not inspect.Parameter.empty:
            # print(f"{param.name}: default={param.default}, type={type(param.default).__name__}")
            temp["default_argument"] = str(param.default)
            temp["data_type"] = type(param.default).__name__
            temp["required"] = False
        else:
            temp["default_argument"] = None
            temp["data_type"] = "None"
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
