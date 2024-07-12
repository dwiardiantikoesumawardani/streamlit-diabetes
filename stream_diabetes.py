import pickle  
import streamlit as st

#Membaca Model 
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

#JudulWeb
st.title('Data Mining Prediksi Diabetes')

#Membagi kolom
col1, col2 = st.columns(2)

with col1:
    Pregnancies = st.text_input('input nilai Pregnancies')
with col2:
    Glucose = st.text_input('input nilai Glucose')
with col1:
    BloodPressure = st.text_input('input nilai BloodPressure')
with col2:
    SkinThickness = st.text_input('input nilai SkinThickness')
with col1:
    Insulin = st.text_input('input nilai Insulin')
with col2:
    BMI = st.text_input('input nilai BMI')
with col1:
    DiabetesPedigreeFuction = st.text_input('input nilai Diabetes Pedigree Funtion')
with col2:
    Age = st.text_input('input nilai Age')

# Code untuk prediksi
diab_diagnosis = ''

# Membuat tombol untuk prediksi
if st.button ('test prediksi diabetes'):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFuction, Age]])
    
    if(diab_prediction[0] == 1):
        diab_diagnosis = 'Pasien Terkena Diabetes'
    else:
        diab_diagnosis = 'Pasien Tidak Terkena Diabetes'
    st.success(diab_diagnosis)
