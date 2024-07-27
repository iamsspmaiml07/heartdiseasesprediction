import pandas as pd
import numpy as np
import streamlit as st
import pickle

loadModel = pickle.load(open('heart_disease_model.sav', 'rb'))

def heartPredictFunction(input_param):
    input_data_as_numpy_array = np.asarray(input_param)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    
    try:
        prediction = loadModel.predict(input_data_reshaped)
        if prediction[0] == 0:
            return 'The person is not suffering from heart disease'
        else:
            return 'The person is suffering from heart disease'
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    st.title('Heart Disease Identification Classification in E-Healthcare')

    # Collect input data
    age = st.number_input('Enter Age', min_value=0, max_value=120, step=1)
    sex = st.selectbox('Select Sex', ['Male', 'Female'])
    cp = st.selectbox('CP Range', ['Typical Angina', 'Atypical Angina', 'Non-Anginal Pain', 'Asymptomatic'])
    trestbps = st.number_input('Blood Pressure', min_value=0, max_value=200, step=1)
    chol = st.number_input('Cholesterol', min_value=0, max_value=600, step=1)
    fbs = st.selectbox('FBS (fasting blood sugar)', ['Yes', 'No'])
    restecg = st.selectbox('RestECG', ['Normal', 'ST-T wave abnormality', 'Left ventricular hypertrophy'])
    thalach = st.number_input('Thalach', min_value=0, max_value=250, step=1)
    exang = st.selectbox('Exang', ['Yes', 'No'])
    oldpeak = st.number_input('Oldpeak', min_value=0.0, max_value=6.0, step=0.1)
    slope = st.selectbox('Slope', ['Upsloping', 'Flat', 'Downsloping'])
    ca = st.number_input('CA', min_value=0, max_value=4, step=1)
    thal = st.selectbox('THAL', ['Normal', 'Fixed Defect', 'Reversable Defect'])

    # Convert categorical inputs to numeric values
    sex = 1 if sex == 'Male' else 0
    cp = {'Typical Angina': 0, 'Atypical Angina': 1, 'Non-Anginal Pain': 2, 'Asymptomatic': 3}[cp]
    fbs = 1 if fbs == 'Yes' else 0
    restecg = {'Normal': 0, 'ST-T wave abnormality': 1, 'Left ventricular hypertrophy': 2}[restecg]
    exang = 1 if exang == 'Yes' else 0
    slope = {'Upsloping': 0, 'Flat': 1, 'Downsloping': 2}[slope]
    thal = {'Normal': 3, 'Fixed Defect': 6, 'Reversable Defect': 7}[thal]

    input_data = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
    
    # Make prediction
    if st.button('Heart Disease Prediction'):
        heart_disease = heartPredictFunction(input_data)
        st.success(heart_disease)

if __name__ == '__main__':
    main()
