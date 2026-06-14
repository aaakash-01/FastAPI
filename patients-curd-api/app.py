from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def hello():
    return {"message": "hello world"}
@app.get("/about")
def about():
    return {"message": "learn fastapi on this website"}