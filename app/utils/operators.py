import inspect

ALLOWED_OPERATORS = {
    "PythonOperator": (1, "airflow.operators.python")
}


def import_from(filename, functionName):
    module = __import__(filename, fromlist=[functionName])
    return getattr(module, functionName)


def get_default_args(func) -> dict:
    signature = inspect.signature(func)
    return {
        k: {"default_argument": v.default if v.default is not inspect.Parameter.empty else "No default argument",
            "data_type": str(v.annotation) if v.annotation is not inspect.Parameter.empty else "No datatype specified"}
        for k, v in signature.parameters.items() if k not in ["self"]
    }


def get_operators() -> dict:
    operators = []
    for operator in ALLOWED_OPERATORS:
        operator_details = {}
        imported_operator = import_from(
            ALLOWED_OPERATORS[operator][1], operator,)
        operator_info = get_default_args(imported_operator.__init__)
        operator_details["args"] = operator_info
        operator_details["name"] = operator
        operator_details["description"] = f"{operator} description."
        operator_details["node_type"] = "operator"
        operator_details["id"] = ALLOWED_OPERATORS[operator][0]
        operators.append(operator_details)

    return operators
