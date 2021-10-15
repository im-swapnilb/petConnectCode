#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
import pandas as pd
import flask as Flask
from flask import request
from flask import render_template
import pickle


# In[12]:


from flask import Flask

app = Flask(__name__)


# In[13]:


@app.route('/')
def home():
    return render_template('index.html')


# In[14]:


# prediction function



# In[16]:


@app.route('/linkedin', methods = ['GET'])
def linkedin():
    # if request.method == 'POST':
    #     to_predict_list = request.form.to_dict()
    #     to_predict_list = list(to_predict_list.values())
    #     if to_predict_list[0] == 'Male':
    #         to_predict_list[0] = 0
    #     else:
    #         to_predict_list[0] = 1
    #     to_predict_list = list(map(float, to_predict_list))
    #     result = ValuePredictor(to_predict_list)
    #     if int(result) == 0:
    #         prediction = 'You are in good shape!!!'
    #     else:
    #         prediction = 'Please, start working out'
        return render_template("linkedin.html")

@app.route('/github', methods = ['GET'])
def github():
    # if request.method == 'POST':
    #     to_predict_list = request.form.to_dict()
    #     to_predict_list = list(to_predict_list.values())
    #     if to_predict_list[0] == 'Male':
    #         to_predict_list[0] = 0
    #     else:
    #         to_predict_list[0] = 1
    #     to_predict_list = list(map(float, to_predict_list))
    #     result = ValuePredictor(to_predict_list)
    #     if int(result) == 0:
    #         prediction = 'You are in good shape!!!'
    #     else:
    #         prediction = 'Please, start working out'
        return render_template("github.html")

@app.route('/medium', methods = ['GET'])
def medium():
    # if request.method == 'POST':
    #     to_predict_list = request.form.to_dict()
    #     to_predict_list = list(to_predict_list.values())
    #     if to_predict_list[0] == 'Male':
    #         to_predict_list[0] = 0
    #     else:
    #         to_predict_list[0] = 1
    #     to_predict_list = list(map(float, to_predict_list))
    #     result = ValuePredictor(to_predict_list)
    #     if int(result) == 0:
    #         prediction = 'You are in good shape!!!'
    #     else:
    #         prediction = 'Please, start working out'
        return render_template("medium.html")
        
@app.route('/instagram', methods = ['GET'])
def instagram():
    # if request.method == 'POST':
    #     to_predict_list = request.form.to_dict()
    #     to_predict_list = list(to_predict_list.values())
    #     if to_predict_list[0] == 'Male':
    #         to_predict_list[0] = 0
    #     else:
    #         to_predict_list[0] = 1
    #     to_predict_list = list(map(float, to_predict_list))
    #     result = ValuePredictor(to_predict_list)
    #     if int(result) == 0:
    #         prediction = 'You are in good shape!!!'
    #     else:
    #         prediction = 'Please, start working out'
        return render_template("instagram.html")

@app.route('/facebook', methods = ['GET'])
def facebook():
    # if request.method == 'POST':
    #     to_predict_list = request.form.to_dict()
    #     to_predict_list = list(to_predict_list.values())
    #     if to_predict_list[0] == 'Male':
    #         to_predict_list[0] = 0
    #     else:
    #         to_predict_list[0] = 1
    #     to_predict_list = list(map(float, to_predict_list))
    #     result = ValuePredictor(to_predict_list)
    #     if int(result) == 0:
    #         prediction = 'You are in good shape!!!'
    #     else:
    #         prediction = 'Please, start working out'
        return render_template("facebook.html")

@app.route('/twitter', methods = ['GET'])
def twitter():
    # if request.method == 'POST':
    #     to_predict_list = request.form.to_dict()
    #     to_predict_list = list(to_predict_list.values())
    #     if to_predict_list[0] == 'Male':
    #         to_predict_list[0] = 0
    #     else:
    #         to_predict_list[0] = 1
    #     to_predict_list = list(map(float, to_predict_list))
    #     result = ValuePredictor(to_predict_list)
    #     if int(result) == 0:
    #         prediction = 'You are in good shape!!!'
    #     else:
    #         prediction = 'Please, start working out'
        return render_template("twitter.html")

# In[17]:


# Main function
if __name__ == "__main__":
    app.run(debug=True)
    app.config['TEMPLATES_AUTO_RELOADED'] = True

