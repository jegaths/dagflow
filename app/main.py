from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from utils.operators import get_operators
from utils.generate_source_string import GenerateSourceString
from utils.dag_to_dagflow import DagToDagFlow
from pydantic import BaseModel
from utils.source_to_json import SourceToJson
from utils.json_to_source import JsonToSource
import json
from collections import defaultdict

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
def root():
    return "Dagflow!"


@app.get("/operators")
def get_operator_list():
    return get_operators()


class Item(BaseModel):
    data: dict


@app.post("/generate_dag")
def generate_dag(data: Item):
    data = data.data
    # Generating the python source code string
    main_str = GenerateSourceString(data).get()
    # Converting the python source code string to json
    obj = SourceToJson(python_code_string=main_str).get()
    # Loading the base dag json with default statements
    with open("./utils/base_dag_json.json", "r") as f:
        base_json = json.load(f)
    # Extending base json with the created json
    base_json["body"].extend(obj["body"])
    # Converting the json back to python source code and saving as a file
    JsonToSource(json_string=json.dumps(base_json, indent=4)).save("/dags/generated_dag.py")
    return {"status": True}


@app.post("/generate_flow")
def generate_flow(file: UploadFile):
    # SourceToJson(python_code_string=file.file.read().decode("utf-8")).save("source_to_json.json")
    data = SourceToJson(python_code_string=file.file.read().decode("utf-8")).json_str()
    dagflow = DagToDagFlow(json_string=data).get()
    return dagflow
    # print(json.dumps(dagflow, indent=4))
