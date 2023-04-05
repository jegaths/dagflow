from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import dagflow
from motor.motor_asyncio import AsyncIOMotorClient

origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_db_client():
    print("Connecting to db..")
    app.mongodb_client = AsyncIOMotorClient("mongodb://mongodb:27017/")
    app.mongodb = app.mongodb_client.dagflow


@app.on_event("shutdown")
async def shutdown_db_client():
    print("Closing db connection")
    app.mongodb_client.close()


@app.get("/")
def root():
    return "Dagflow!"


app.include_router(dagflow.router)
