from fastapi import APIRouter, Request, status
from pydantic import BaseModel
from utils.json_to_source import JsonToSource
from utils.generate_source_string import GenerateSourceString
from utils.source_to_json import SourceToJson
import json
from utils.dag_to_dagflow import DagToDagFlow
from utils.source_to_json import SourceToJson
from fastapi import UploadFile
import os
from utils.model.pipeline_model import COLLECTION, Pipeline
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import datetime
from utils.model.operator_model import Operator

router = APIRouter(prefix="/dagflow", tags=["dagflow"])


@router.get("/operators")
async def get_operator_list(request: Request):
    collection = request.app.mongodb.get_collection("operators")
    projection = {"_id": 0}
    document = await collection.find({}, projection).to_list(length=None)
    try:
        data = [Operator(**doc) for doc in document]
    except ValueError as e:
        print(str(e))
    return data
    # return document


class Item(BaseModel):
    data: dict


@router.post("/generate_dag")
async def generate_dag(data: Item):
    data = data.data
    # Generating the python source code string
    main_str = await GenerateSourceString(data).get()
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
async def generate_flow(file: UploadFile):
    data = SourceToJson(python_code_string=file.file.read().decode("utf-8")).json_str()
    dagflow = DagToDagFlow(json_string=data)
    dagflow = await dagflow.generate_dagflow()
    dagflow.data.pipeline_name = os.path.splitext(file.filename)[0]
    return dagflow.data


@router.post("/save_pipeline")
async def save_pipeline(request: Request, pipeline: Pipeline):
    pipeline = pipeline.data
    collection = request.app.mongodb.get_collection(COLLECTION)
    filter = {"pipeline_id": pipeline.pipeline_id}
    data = jsonable_encoder(pipeline)
    data["updated_at"] = datetime.datetime.now().isoformat()
    result = await collection.update_one(filter, {"$set": jsonable_encoder(data)}, upsert=True)
    # print("Number of documents matched: ", result.matched_count)
    # print("Number of documents modified: ", result.modified_count)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Pipeline saved successfully", "pipeline": pipeline.pipeline_name},
    )


@router.get("/get_recent_pipeline_names/{number_of_pipelines}")
async def get_pipelines(request: Request, number_of_pipelines: int):
    collection = request.app.mongodb.get_collection(COLLECTION)
    projection = {"_id": 0, "pipeline_id": 1, "pipeline_name": 1}
    # document = await collection.find({}, projection).to_list(length=None)
    # try:
    #     data = Pipeline(**{"data": document[0]})
    # except ValueError as e:
    #     print(str(e))
    # return data
    collection = request.app.mongodb.get_collection(COLLECTION)
    pipelineNames = (
        await collection.find({}, projection).limit(number_of_pipelines).sort("updated_at", -1).to_list(length=None)
    )
    return pipelineNames


@router.post("/get_pipeline")
async def get_pipelines(request: Request, pipeline: dict):
    collection = request.app.mongodb.get_collection(COLLECTION)
    projection = {"_id": 0, "updated_at": 0}
    query = {"pipeline_id": pipeline["pipeline_id"]}
    document = await collection.find(query, projection).to_list(length=None)
    try:
        data = Pipeline(**{"data": document[0]})
    except ValueError as e:
        print(str(e))
    return data.data
