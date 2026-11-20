from pathlib import Path

from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd
from pydantic import BaseModel

app = FastAPI()


class StudentData(BaseModel):
    study_hours: float
    attendance: float
    previous_marks: float


MODEL_PATH = Path(__file__).resolve().parent / "Models" / "student_model.pkl"
model = joblib.load(MODEL_PATH)


@app.get("/")
def home():
    return {"message": "Welcome to the naveen Performance Prediction API!"}


@app.post("/predict")
def predict(Student: StudentData):
    try:
            
        input_data = pd.DataFrame([{
            "study_hours": Student.study_hours,
            "attendance": Student.attendance,
            "previous_marks": Student.previous_marks
        }])
        prediction = model.predict(input_data)
        return{"prediction_result":prediction[0]}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")