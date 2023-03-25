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


@app.post("/run_pipeline")
def run_pipeline(data: Item):
    data = data.data
    import_str = ""
    arg_str = ""
    for key in data["operators"]:
        operator = data["operators"][key]
        import_str += f"""from {operator['import_path']} import {operator['name']}
"""
        python_str = f"""{operator['name']}("""
        for k, v in operator["args"].items():
            if (v != ""):
                python_str += f"""{k} = {v},""" if k == "python_callable" else f"""{k} = '{v}',"""
        # * Adding dag as an argument
        python_str += f"""dag = dag"""
        python_str += """)\n"""
        # * Adding to main arg_str with a operator variable
        arg_str += f'{key} = {python_str}'

    global_str = ""
    if (data['global'] != ""):
        global_str += f"""{data["global"]}
"""

    main_str = import_str + global_str + arg_str
    obj = SourceToJson(python_code_string=main_str).get()
    with open("./utils/base_dag_json.json", "r") as f:
        base_json = json.load(f)
    base_json['body'].extend(obj['body'])
    print(JsonToSource(json_string=json.dumps(base_json, indent=4)).save("generated_dag.py"))


#     if ("global" in data["args"].keys()):
#         python_str += f"""{data["args"]["global"]["default_argument"]}
# """
#     python_str += f"""{data['name']}("""
    # for k, v in data["args"].items():
    #     if (v["default_argument"] != ""):
    #         if (k == "global"):
    #             continue
    #         python_str += f"""{k} = {v["default_argument"]},"""
    # python_str += f""")"""
#     print(python_str)
#     obj = SourceToJson(python_code_string=python_str).get()
#     with open("./utils/base_dag_json.json", "r") as f:
#         base_json = json.load(f)

#     base_json['body'].extend(obj['body'])
#     print(JsonToSource(json_string=json.dumps(base_json, indent=4)).save("generated_dag.py"))

    # print(data)
    # python_callable = data["python_callable"]
    # obj = SourceToJson(python_code_string=python_callable).get()

    # base_last_line_number = 22
    # obj['body'][0]["lineno"] += base_last_line_number
    # obj['body'][0]["end_lineno"] += base_last_line_number

    return {"status": True}


# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
