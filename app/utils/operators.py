import inspect

from utils.model.operator_model import Operator, Args

from utils.app import app


def import_from(filename, functionName):
    module = __import__(filename, fromlist=[functionName])
    return getattr(module, functionName)


async def get_operator_details(operator_name: str = None, projection={}) -> Operator:
    collection = app.mongodb.get_collection("operators")
    projection = {**{"_id": 0}, **projection}
    if operator_name is None:
        documents = await collection.find({}, projection).to_list(None)
        return documents
    document = await collection.find_one({"name": operator_name}, projection)
    return document


def get_default_args_v2(func) -> dict[str, Args]:
    # To get if an argument is mandatory to create an object in Python, you can check if the argument has a default value of inspect.Parameter.empty. If it does not have a default value, then the argument is mandatory.
    sig = inspect.signature(func)
    res = {}
    for param in sig.parameters.values():
        if param.name in ["self", "args", "kwargs"]:
            continue
        temp = Args(**{})
        if param.default is not inspect.Parameter.empty:
            datatype = "" if type(param.default).__name__ == "NoneType" else type(param.default).__name__
            if datatype == "int":
                __default_argument = int(param.default)
            elif datatype == "None" or datatype == "":
                __default_argument = ""
            else:
                __default_argument = str(param.default)
            temp.default_argument = __default_argument
            temp.data_type = datatype
            temp.required = False
        else:
            temp.default_argument = ""
            temp.data_type = ""
            temp.required = True
        res[param.name] = temp
    return res


def generate_operators(operator: Operator) -> Operator:
    imported_operator = import_from(operator.import_path, operator.name)
    operator_info = get_default_args_v2(imported_operator.__init__)
    operator.args = {**operator.args, **operator_info}
    return operator
