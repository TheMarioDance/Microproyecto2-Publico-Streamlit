#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
from src.ModelController import ModelController

st.set_page_config(page_title="Clasificador ODS", page_icon="🌍", layout="centered")

st.title("Clasificador de textos según ODS")
st.write(
    "Esta aplicación permite ingresar un texto libre y predecir el Objetivo de Desarrollo "
    "Sostenible (ODS) asociado, utilizando el modelo entrenado en el microproyecto."
)

controller = ModelController()

texto_usuario = st.text_area(
    "Ingrese un texto:",
    height=200,
    placeholder="Escriba aquí un texto relacionado con desarrollo sostenible..."
)

if st.button("Clasificar"):
    if texto_usuario.strip() == "":
        st.warning("Por favor ingrese un texto antes de clasificar.")
    else:
        prediccion = controller.predict(texto_usuario)
        st.success(f"ODS predicho: {prediccion}")

