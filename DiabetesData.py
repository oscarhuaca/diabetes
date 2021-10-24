# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 07:18:11 2021

@author: dreve
"""
from pydantic import BaseModel

class Diabetesdata(BaseModel):
    Pregnancies: float 
    Glucose: float 	
    BloodPressure: float 	
    SkinThickness: float 	
    Insulin: float 	
    BMI: float 
    DiabetesPedigreeFunction: float 	
    Age: float 
