from fastapi import FastAPI, Depends
from .database import Base,engine,get_db
from . import models,schemas,crud
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)


app=FastAPI(title="URL-Shortener API")
@app.get("/")
def root():
    return {"message": "URL-shorterner api is running!"}

@app.post("/shorten",response_model=schemas.URLResponse,status_code=201)
def shorten_url(data:schemas.URLCreate,db:Session=Depends(get_db)):
    url=crud.create_short_url(db,str(data.url))
    return{
        "short_code":url.short_code,
        "short_url":f"http://localhost:8000/{url.short_code}"
    }
