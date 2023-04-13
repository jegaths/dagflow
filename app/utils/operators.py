import inspect

import pydantic
from utils.model.operator_model import Operator, Args
from utils.app import app
import ast
import os
import importlib


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


def generate_operators(operator: Operator) -> tuple[Operator, bool]:
    status = False
    try:
        imported_operator = import_from(operator.import_path, operator.name)
        operator_info = get_default_args_v2(imported_operator.__init__)
        operator.args = {**operator.args, **operator_info}
        status = True
    except ModuleNotFoundError:
        print(f"ModuleNotFoundError => {operator.name}")
    return operator, status


def get_operator_list() -> list[str]:
    class Modules(pydantic.BaseModel):
        module: str
        sub_module: str

    def get_class_name(file_path):
        with open(file_path, "r") as file:
            # Parse the Python file as an abstract syntax tree (AST)
            tree = ast.parse(file.read())

            # Iterate through all nodes in the AST
            for node in tree.body:
                # Check if the node is a class definition
                if isinstance(node, ast.ClassDef):
                    for base in node.bases:
                        # Check if the base class is BaseOperator
                        if isinstance(base, ast.Name) and base.id == "BaseOperator":
                            # Return the name of the class
                            return node.name

    modules = [Modules(**{"module": "airflow", "sub_module": "operators"})]
    operators_dir = os.path.join(
        os.path.dirname(importlib.import_module(modules[0].module).__file__), modules[0].sub_module
    )

    operator_lists = []

    index = 1
    for file_name in os.listdir(operators_dir):
        # Skip non-Python files and __init__.py
        if not file_name.endswith(".py") or file_name == "__init__.py":
            continue

        class_name = get_class_name(operators_dir + "/" + file_name)
        file_name_without_extension = os.path.splitext(file_name)[0]
        if class_name != None:
            operator_lists.append(
                {
                    "id": index,
                    "name": class_name,
                    "import_path": modules[0].module + "." + modules[0].sub_module + "." + file_name_without_extension,
                }
            )
            index += 1
    return operator_lists
