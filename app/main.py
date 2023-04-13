from fastapi.middleware.cors import CORSMiddleware
from routers import dagflow
from motor.motor_asyncio import AsyncIOMotorClient
from utils.operators import generate_operators, get_operator_list
from utils.model.operator_model import Operator
from fastapi.encoders import jsonable_encoder
from pymongo import UpdateOne

from utils.app import app

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
    app.mongodb_client = AsyncIOMotorClient("mongodb://mongodb:27017/")
    app.mongodb = app.mongodb_client.dagflow

    collection = app.mongodb.get_collection("operators")
    operators = get_operator_list()
    # operators = [
    #     {"id": 1, "name": "PythonOperator", "import_path": "airflow.operators.python"},
    #     {"id": 2, "name": "BashOperator", "import_path": "airflow.operators.bash"},
    # ]

    data = []
    for operator in operators:
        generated_operator, status = generate_operators(Operator.parse_obj(operator))
        if status:
            filter = {"id": generated_operator.id}
            data.append(UpdateOne(filter, {"$set": jsonable_encoder(generated_operator)}, upsert=True))

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
