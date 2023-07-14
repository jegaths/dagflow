from fastapi.middleware.cors import CORSMiddleware
from routers import dagflow
from motor.motor_asyncio import AsyncIOMotorClient
from utils.operators import generate_operators, get_operator_list
from utils.model.operator_model import Operator
from fastapi.encoders import jsonable_encoder
from pymongo import UpdateOne
import os

from utils.app import app

import pyroscope

pyroscope.configure(
    application_name="dagflow-api",
    server_address="http://pyroscope:4040",
    oncpu=False,
    detect_subprocesses=True,

    tags={
        "region": "all",
    },
)

origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_db_client():
    # print(get_operator_list())

    print("Connecting to db..")
    # Connecting to mongodb on startup and initializing the database. Need to generate the operator lists on startup.
    # TODO: Have to take the operator list from somewhere else. Maybe a config file or something. Also have to create a list of default operators.
    mongodb_url = os.getenv("DAGFLOW_MONGODB_URL", "mongodb://mongodb:27017/")
    print(mongodb_url)
    app.mongodb_client = AsyncIOMotorClient(mongodb_url)
    app.mongodb = app.mongodb_client.dagflow

    collection = app.mongodb.get_collection("operators")
    operators = get_operator_list()
    data = []
    for operator in operators:
        generated_operator, status = generate_operators(Operator.parse_obj(operator))
        if status:
            filter = {"id": generated_operator.id}
            data.append(
                UpdateOne(
                    filter, {"$set": jsonable_encoder(generated_operator)}, upsert=True
                )
            )

    await collection.bulk_write(data)
    print("Filled operators..")


@app.on_event("shutdown")
async def shutdown_db_client():
    print("Closing db connection")
    app.mongodb_client.close()


@app.get("/")
def root():
    return get_operator_list()
    return "Dagflow!"


app.include_router(dagflow.router)
