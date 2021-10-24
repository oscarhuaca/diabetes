# 1. Library imports
import uvicorn
from fastapi import FastAPI
from DiabetesData import Diabetesdata
import numpy as np
import pickle
import pandas as pd

# Create the app object
app = FastAPI()


# Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'Mensaje': 'Sistema de Clasificación'}

#    Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{text}')
def get_text(text: str):
    return {'El texto es': f'{text}'}

# Expose the prediction functionality, make a prediction from the passed
#  JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_diabetes(data:Diabetesdata):
    
    data = data.dict()
    
    Pregnancies=data['Pregnancies']
    Glucose= data['Glucose']
    BloodPressure=data['BloodPressure']
    SkinThickness= data['SkinThickness']
    Insulin= data['Insulin']
    BMI= data['BMI']
    DiabetesPedigreeFunction= data['DiabetesPedigreeFunction']
    Age= data['Age']
    
    xin = np.array([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]).reshape(1,8)

    prediction = model.predict(xin)
    yout = labels[prediction[0]]
    
    return {
        'prediction': yout
    }

#    Run the API with uvicorn
#    Will run on http://127.0.0.1:8000


pkl_filename = "diabetes_model.pkl"
with open(pkl_filename, 'rb') as file:
    model = pickle.load(file)

labels = ['Sano','Diabetes']  

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload