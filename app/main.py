from fastapi import FastAPI
from .database import Base,engine
from . import models

Base.metadata.create_all(bind=engine)


app=FastAPI(title="URL-Shortener API")
@app.get("/")
def root():
    return {"message": "URL-shorterner api is running!"}