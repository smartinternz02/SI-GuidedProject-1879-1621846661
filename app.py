# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 23:34:10 2020

@author: Madhav Rathi
"""


from flask import Flask, request, render_template
import numpy as np
import re
import requests

app = Flask(__name__)

def check(output):

    url = "https://image-to-text2.p.rapidapi.com/cloudVision/imageToText"
    
    querystring = {"source":output,"sourceType":"url"}
    
    payload = '''{\r\n    \"source\": "'''+output+'''" ,\r\n    \"sourceType\": \"url\"\r\n}'''
    headers = {
        'content-type': "application/json",
        'x-rapidapi-key': "fbd4199c1amsh2c93fd54d73d474p1d7c4cjsn786fe34bf93d",
        'x-rapidapi-host': "image-to-text2.p.rapidapi.com"
        }
    
    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    
    print(response.text)
    return (response.json()['text'])
    

#home page
@app.route('/')
def home():
    return render_template('base.html')

#Summarizer page
@app.route('/predict',methods=['POST'])
def predict():
    output=request.form['output']
    text=check(output)
    return render_template('base.html',output=text)

    
if __name__ == "__main__":
    app.run(debug=True)



