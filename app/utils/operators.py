import inspect

import pydantic
from utils.model.operator_model import Operator, Args
from utils.app import app
import ast
import os
import importlib
import json


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
        # if param.name in ["self", "args", "kwargs"]:
        if param.name in ["self"]:
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
        # TODO Some valid operators are getting ModuleNotFoundError, need to check why
        print(f"ModuleNotFoundError => {operator.name}")
    return operator, status


def get_operator_list() -> list[str]:
    class Modules(pydantic.BaseModel):
        module: str
        sub_module: str

    base_inherited_classes = ["BaseOperator", "GoogleCloudBaseOperator"]

    # Function to get the name of the class from a Python file which inherits from BaseOperator
    def get_class_name(file_path) -> list[str]:
        ops_list = []
        with open(file_path, "r") as file:
            # Parse the Python file as an abstract syntax tree (AST)
            # print(file.read())
            tree = ast.parse(file.read())
            # Iterate through all nodes in the AST
            for node in tree.body:
                # Check if the node is a class definition
                if isinstance(node, ast.ClassDef):
                    for base in node.bases:
                        # Check if the base class is BaseOperator
                        # if isinstance(base, ast.Name) and base.id in base_inherited_classes:
                        if isinstance(base, ast.Name) and "operator" in base.id.lower():
                            # Return the name of the class
                            ops_list.append(node.name)
                            # return node.name
        return ops_list

    # Function to find folders which have a subfolder called operators
    def find_operators_folder(base_dir):
        operator_dirs = []
        for dirpath, dirnames, _ in os.walk(base_dir):
            if "operators" in dirnames:
                operator_dirs.append(
                    Modules(
                        **{
                            "module": f'airflow.providers.{dirpath.split("providers/",1)[1].replace("/",".")}',
                            "sub_module": "operators",
                        }
                    )
                )
        return operator_dirs

    # Function to get the list of operators from a directory
    def get_operator_list_from_dir(operator, operator_lists):
        operators_dir = os.path.join(
            os.path.dirname(importlib.import_module(operator.module).__file__), operator.sub_module
        )
        for file_name in os.listdir(operators_dir):
            # Skip non-Python files and __init__.py
            if not file_name.endswith(".py") or file_name == "__init__.py":
                continue

            file_name_without_extension = os.path.splitext(file_name)[0]
            # if(file_name_without_extension == "postgres"):
            #     print("************************")
            #     print(operators_dir)
            #     print(file_name_without_extension)
            #     print(operators_dir + "/" + file_name)
            #     print("************************")
            # else:
            #     continue
            #     # print("---------------------------------")
            #     # print(operators_dir)
            #     # print(file_name_without_extension)
            #     # print("---------------------------------")
            class_names = get_class_name(operators_dir + "/" + file_name)
            # print(file_name_without_extension)
            for class_name in class_names:
                import_path = operator.module + "." + operator.sub_module + "." + file_name_without_extension
                operator_lists.append(
                    {
                        "id": f"{file_name_without_extension}_{import_path}_{class_name}",
                        "name": class_name,
                        "import_path": import_path,
                    }
                )

    # Generate operators from core module
    core_operator = Modules(**{"module": "airflow", "sub_module": "operators"})
    operator_lists = []
    get_operator_list_from_dir(core_operator, operator_lists)

    # Generate operators from providers module
    provider_operator = find_operators_folder(
        os.path.join(os.path.dirname(importlib.import_module("airflow").__file__), "providers")
    )
    for provider in provider_operator:
        get_operator_list_from_dir(provider, operator_lists)
    return operator_lists
