import numpy as np
import streamlit as st
import pickle
import os

working_dir = os.path.dirname(os.path.abspath(__file__))

heart_disease_model = pickle.load(open(f'{working_dir}/models/heart_disease_model.sav', 'rb'))

def main():
    st.title('Heart Disease Identification Classification In E-Healthcare')

    # Input fields
    age = st.text_input('Enter Age')
    sex = st.text_input('Enter Sex')
    cp = st.text_input('CP Range')
    trestbps = st.text_input('Blood Pressure')
    chol = st.text_input('Cholesterol')
    fbs = st.text_input('FBS')
    restecg = st.text_input('RestECG')
    thalach = st.text_input('Thalach')
    exang = st.text_input('Exang')
    oldpeak = st.text_input('Oldpeak')
    slope = st.text_input('Slope')
    ca = st.text_input('CA')
    thal = st.text_input('THAL')

    # Code for Prediction
    heart_diagnosis = ''

    # Creating a button for Prediction
    if st.button('Heart Diseases'):
        try:
            # Convert inputs to float
            user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            user_input = [float(x) for x in user_input]

            # Make prediction
            heart_prediction = heart_disease_model.predict([user_input])

            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'

        except ValueError as e:
            heart_diagnosis = f"Input error: {e}"
        except Exception as e:
            heart_diagnosis = f"An error occurred: {e}"

    st.success(heart_diagnosis)

if __name__ == '__main__':
    main()
