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


@app.get("/operators")
def get_operatords():
    return get_operators()


class Item(BaseModel):
    data: dict


@app.post("/run_pipeline")
def run_pipeline(data: Item):
    data = data.data
    python_callable = data["python_callable"]
    obj = SourceToJson(python_code_string=python_callable).get()
    with open("./utils/base_dag_json.json", "r") as f:
        base_json = json.load(f)

    # base_last_line_number = 22
    # obj['body'][0]["lineno"] += base_last_line_number
    # obj['body'][0]["end_lineno"] += base_last_line_number
    base_json['body'].extend(obj['body'])
    print(JsonToSource(json_string=json.dumps(base_json, indent=4)).save("generated_dag.py"))
    return {"status": True}


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
