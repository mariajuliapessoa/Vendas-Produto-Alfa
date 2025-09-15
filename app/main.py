from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Forecast-Produto-Alfa")

class RequestLastN(BaseModel):
    horizon: int = 14

model = None
@app.on_event("startup")
def load_model():
    global model
    try:
        model = joblib.load("models/lgbm_prod_alfa.pkl")
    except Exception:
        model = None

@app.post("/predict")
def predict(req: RequestLastN):
    # endpoint demo: expects that a model exists and data is present in storage
    if model is None:
        return {"error":"modelo não carregado (execução demo)."}
    # For demo, return zeros or a placeholder
    return {"horizon": req.horizon, "predictions": [0]*req.horizon}
