import uvicorn
from fastapi import Depends, FastAPI,Request, Form
from fastapi.templating import Jinja2Templates
from BankNote import Note
import numpy as np
import pandas as pd
from Model_Training import classifier

app = FastAPI()
templates = Jinja2Templates(directory="templates/")

@app.get('/')
def index():
    return {'message':'hello'}

# this function does is the prediction of passed JSON data and return predicted Note with the confidence
# 0 = yes
# 1 = no

@app.get("/form")
def form_post(request: Request):
    prediction = "Enter the details"
    return templates.TemplateResponse('index.html', context={'request': request, 'prediction': prediction})

@app.post('/form')
def predict_banknote(request:Request, data : Note = Depends()): # take the input in format of the class BankNote
    # def predict_banknote(data : Note)
    variables ={}
    #data = data.dict()
    #print("Hello")
    variables.update({"variance": data.variance})
    variables.update({"skewness": data.skewness})
    variables.update({"curtosis": data.curtosis})
    variables.update({"entropy": data.entropy})
    # variance = data['variance']
    # skewness = data['skewness']
    # curtosis = data['curtosis']
    # entropy = data['entropy']

    # value = classifier.predict([["variance",skewness,curtosis,entropy]])
    value = classifier.predict([[variables.get("variance"),variables.get("skewness"), variables.get("curtosis"),variables.get("entropy")]])

    if(value>0.5):
        prediction = "False, not a bank Note"
    else:
        prediction = "True, It is a bank note"
    
    return templates.TemplateResponse('result.html', context={'request': request, 
                                                            'variance':variables.get("variance"),
                                                            'skewness':variables.get("skewness"),
                                                            'curtosis':variables.get("curtosis"),
                                                            'entropy':variables.get("entropy"),
                                                            'prediction': prediction})
