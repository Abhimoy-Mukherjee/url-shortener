from fastapi import FastAPI

app=FastAPI(title="URL-Shortener API")
@app.get("/")
def root():
    return {"message": "URL-shorterner api is running!"}