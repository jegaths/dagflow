from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils.operators import get_operators
from utils.generate_source_string import GenerateSourceString
import uvicorn
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
def get_operatords():
    return "Dagflow!"


@app.get("/operators")
def get_operatords():
    return get_operators()


class Item(BaseModel):
    data: dict


def get_relation(root_node, edges, relation):
    for edge in edges:
        if (edge["source"] == root_node):
            relation[edge["target"]] = {}
            get_relation(edge["target"], edges, relation[edge["target"]])


@app.post("/generate_dag")
def generate_dag(data: Item):
    data = data.data

    edges = data["react_flow_data"]["edges"]

    sources = set()
    targets = set()
    for edge in edges:
        sources.add(edge["source"])
        targets.add(edge["target"])

    roots = list(sources - targets)

    orphans = list(set(data["operators"].keys()) - set(list(sources) + list(targets)))

    relation = {}
    for root in roots:
        relation[root] = {}
        get_relation(root, edges, relation[root])

    print("*"*100)
    print(f"Relation =========> {json.dumps(relation, indent=4, sort_keys=True, default=str)}")
    print(orphans)
    print("*"*100)

    # print("*"*100)
    # print(list(targets - sources))
    # print(f"Targets =========> {targets}")
    # print(f"Sources =========> {sources}")
    # print(f"Root =========> {root}")
    # print("*"*100)

    # print(json.dumps(data, indent=4, sort_keys=True, default=str))

    # Generating the python source code string
    main_str = GenerateSourceString.get(data)
    # Converting the python source code string to json
    obj = SourceToJson(python_code_string=main_str).get()
    # Loading the base dag json with default statements
    with open("./utils/base_dag_json.json", "r") as f:
        base_json = json.load(f)
    # Extending base json with the created json
    base_json['body'].extend(obj['body'])
    # Converting the json back to python source code and saving as a file
    JsonToSource(json_string=json.dumps(base_json, indent=4)).save("generated_dag.py")
    return {"status": True}
