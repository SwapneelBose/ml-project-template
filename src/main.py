from fastapi import FastAPI

from src.model import predict

app = FastAPI(title="ML Project Template")


@app.get("/")
def read_root():
    return {"message": "Hello, World! FastAPI is running 🚀"}


@app.get("/predict")
def get_prediction(x: float):
    return {"input": x, "prediction": predict(x)}
