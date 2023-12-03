## Import libraries
import streamlit as st
import pandas as pd
import numpy as np
from tensorflow import keras
from keras import models 
from keras.models import load_model
from sklearn.preprocessing import StandardScaler
import pickle


## Load the trained model
model = load_model('model.h5')

def main():
    st.title("Breast Cancer Prediction App")
    st.markdown("""
        :dart: This application serves as a valuable tool for medical professionals, particularly doctors, aiding in the prediction of whether a patient's breast cancer is malignant tumor( higher likelihood of cancer) or benign tumor(non-cancerous). As a doctor, you should input essential patient vitals and details related to breast cancer, allowing the system to generate predictions based on advanced algorithms. 
    """)
    st.warning("Utilize the menu below to input the necessary cancer details and patient information for accurate predictions.")

    ## Create input fields for tumor features
    radius_mean = st.number_input('Radius Mean:', min_value=0.0, max_value=30.0, value=0.0)
    perimeter_mean = st.number_input('Perimeter Mean:', min_value=0.0, max_value=200.0, value=0.0)
    area_mean = st.number_input('Area Mean:', min_value=0.0, max_value=2500.0, value=0.0)
    compactness_mean = st.number_input('Compactness Mean:', min_value=0.0, max_value=1.0, value=0.0)
    concavity_mean = st.number_input('Concavity Mean:', min_value=0.0, max_value=1.0, value=0.0)
    concave_points_mean = st.number_input('Concave Points Mean:', min_value=0.0, max_value=1.0, value=0.0)
    radius_se = st.number_input('Radius SE:', min_value=0.0, max_value=30.0, value=0.0)
    perimeter_se = st.number_input('Perimeter SE:', min_value=0.0, max_value=200.0, value=0.0)
    area_se = st.number_input('Area SE:', min_value=0.0, max_value=2500.0, value=0.0)
    radius_worst = st.number_input('Radius Worst:', min_value=0.0, max_value=30.0, value=0.0)
    perimeter_worst = st.number_input('Perimeter Worst:', min_value=0.0, max_value=200.0, value=0.0)
    area_worst = st.number_input('Area Worst:', min_value=0.0, max_value=2500.0, value=0.0)
    compactness_worst = st.number_input('Compactness Worst:', min_value=0.0, max_value=1.0, value=0.0)
    concavity_worst = st.number_input('Concavity Worst:', min_value=0.0, max_value=1.0, value=0.0)
    concave_points_worst = st.number_input('Concave Points Worst:', min_value=0.0, max_value=1.0, value=0.0)



    ##  Make prediction when the user clicks the button
    if st.button('Predict Breast Cancer'):
        prediction = model.predict([[radius_mean, perimeter_mean, area_mean, compactness_mean, concavity_mean, concave_points_mean, radius_se, perimeter_se, area_se, radius_worst, perimeter_worst, area_worst, compactness_worst, concavity_worst, concave_points_worst]])
        result = np.round(prediction[0, 0], 2)
        st.info(f"Probability of Malignancy: {result}")

        # Display a message based on the malignancy probability (result)
        if result > 0.5:
            st.success("Malignant: Cancer is likely to be malignant.")
        else:
            st.success("Benign: Cancer is likely to be benign.")

        # Confidence factor
        confidence_factor = 2.58 * np.sqrt((result * (1 - result)) / 1) 
        st.write(f"Confidence Factor: {confidence_factor}")



  

1
if __name__ == "__main__":
    main()
