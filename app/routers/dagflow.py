from fastapi import APIRouter, Request, status
from utils.operators import get_operators
from pydantic import BaseModel
from utils.json_to_source import JsonToSource
from utils.generate_source_string import GenerateSourceString
from utils.source_to_json import SourceToJson
import json
from utils.dag_to_dagflow import DagToDagFlow
from utils.source_to_json import SourceToJson
from fastapi import UploadFile
import os
from utils.model.pipeline_modal import COLLECTION, Pipeline
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

router = APIRouter(prefix="/dagflow", tags=["dagflow"])


@router.get("/operators")
def get_operator_list():
    return get_operators()


class Item(BaseModel):
    data: dict


@router.post("/generate_dag")
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
    JsonToSource(json_string=json.dumps(base_json, indent=4)).save(f"/dags/{data['pipeline_name']}.py")
    return {"status": True}


@router.post("/generate_flow")
def generate_flow(file: UploadFile):
    data = SourceToJson(python_code_string=file.file.read().decode("utf-8")).json_str()
    dagflow = DagToDagFlow(json_string=data).get()
    dagflow["pipeline_name"] = os.path.splitext(file.filename)[0]
    return dagflow


@router.post("/save_pipeline")
async def save_pipeline(request: Request, pipeline: Pipeline):
    pipeline = pipeline.data
    collection = request.app.mongodb.get_collection(COLLECTION)
    filter = {"pipeline_name": pipeline.pipeline_name}
    result = await collection.update_one(filter, {"$set": jsonable_encoder(pipeline)}, upsert=True)
    print("Number of documents matched: ", result.matched_count)
    print("Number of documents modified: ", result.modified_count)
    print("Upserted ID: ", result.upserted_id)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"message": "Pipeline saved successfully", "pipeline": pipeline.pipeline_name},
    )