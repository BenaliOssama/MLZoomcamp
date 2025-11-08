from fastapi import FastAPI
from pydantic import BaseModel
import pickle

# Load the trained model
with open("pipeline_v1.bin", "rb") as f:
    model = pickle.load(f)

# Define input schema
class Client(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float

app = FastAPI()

@app.post("/predict")
def predict(client: Client):
    record = client.dict()
    proba = model.predict_proba([record])[0, 1]
    return {"conversion_probability": round(proba, 3)}

