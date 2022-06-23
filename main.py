from fastapi import FastAPI


app = FastAPI(title="Employee management")


@app.get("/")
def welcome():
    return {"Hello": "World"}
