from fastapi import APIRouter,HTTPException
import numpy as np

from app.models.input_data import IrisData
from app.services.load_model import load_model

router = APIRouter()

model_trained = load_model()

@router.post("/predict")
def predict(data: IrisData):
    try:
        input_data = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
        
        prediction = model_trained.predict(input_data)

        class_name = model_trained.target_names[prediction[0]]
        
        return {"prediction": class_name}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))