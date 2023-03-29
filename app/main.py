from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils.operators import get_operators
import uvicorn
from pydantic import BaseModel
from utils.source_to_json import SourceToJson
from utils.json_to_source import JsonToSource
import json

origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def get_operatords():
    return "Dagflow!"


@app.get("/operators")
def get_operatords():
    return get_operators()


class Item(BaseModel):
    data: dict


@app.post("/generate_dag")
def generate_dag(data: Item):
    data = data.data
    # Variable to store import statements
    import_str = []
    # Variable to store operators
    arg_str = ""
    for key in data["operators"]:
        operator = data["operators"][key]
        import_str.append(f"""from {operator['import_path']} import {operator['name']}
""")
        # Variable to store operator arguments
        python_str = f"""{operator['name']}("""
        for k, v in operator["args"].items():
            if (v != ""):
                python_str += f"""{k} = {v},""" if k == "python_callable" else f"""{k} = '{v}',"""
        # * Adding dag as an argument
        python_str += f"""dag = dag"""
        python_str += """)\n"""
        # * Adding to main arg_str with a operator variable
        arg_str += f'{key} = {python_str}'

    # Variable to store global statements and args
    global_str = ""
    if (data['global'] != ""):
        global_str += f"""{data["global"]}
"""

    # Combining all the strings
    main_str = "".join(list(set(import_str))) + global_str + arg_str
    # Converting the python string to json
    obj = SourceToJson(python_code_string=main_str).get()
    # Loading the base dag json with default statements
    with open("./utils/base_dag_json.json", "r") as f:
        base_json = json.load(f)
    # Extending base json with the created json
    base_json['body'].extend(obj['body'])
    # Converting the json back to python source code and saving as a file
    JsonToSource(json_string=json.dumps(base_json, indent=4)).save("generated_dag.py")
    return {"status": True}


# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
