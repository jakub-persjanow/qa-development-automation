from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from routes import router as members_router

config = dotenv_values(".env")

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["ATLAS_URI"], server_api=ServerApi("1"))
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(members_router, tags=["members"], prefix="/members")