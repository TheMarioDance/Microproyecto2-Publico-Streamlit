#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import joblib

class ModelController:
    def __init__(self, model_path="resources/models/model.joblib"):
        self.model = joblib.load(model_path)

    def predict(self, text):
        pred = self.model.predict([text])[0]
        return pred

