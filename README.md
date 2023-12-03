
## Breast Cancer Prediction App

This application serves as a valuable tool for the prediction of whether a patient's breast cancer is malignant or benign. You can input essential patient details related to breast cancer, to allow the system to generate predictions based on implemented algorithms.

## Project Overview

The Breast Cancer Prediction App leverages deep learning models to predict the nature of breast tumors. It provides a user-friendly interface for everyone to input patient details, facilitating quick and informed decisions.

## Project Structure
- `Group2_Breast_Cancer_Prediction.ipynb`: Jupyter Notebook containing the Python code for the project.
- **DNN.py/:** Contains the Streamlit web application code.
- **model.h5/:** Holds the trained neural network.


## Getting Started

Follow these steps to set up and run the application:

### Running the Jupyter Notebook

1. Open `Group2_Breast_Cancer_Prediction.ipynb` using Jupyter Notebook or Google Colab.
2. Run each cell sequentially to train the model, perform data analysis, and evaluate the model.

### Deploying the Streamlit Web Application

1. Install the required libraries: `pip install streamlit, scikit-learn, pandas, numpy, keras`.
2. Run the Streamlit application in the terminal: `streamlit run DNN.py`.
3. Open a web browser and go to the local host link provided.
4. Enter the required health details, and the application will predict the likelihood of heart disease.


## Input Features

- `Radius Mean`
- `Perimeter Mean`
- `Area Mean`
- `Compactness Mean`
- `Concavity Mean`
- `Concave Points Mean`
- `Radius SE`
- `Perimeter SE`
- `Area SE`
- `Radius Worst`
- `Perimeter Worst`
- `Area Worst`
- `Compactness Worst`
- `Concavity Worst`
- `Concave Points Worst`

## Predictions

- **Benign Prediction:** Indicates a non-cancerous tumor.
- **Malignant Prediction:** Indicates a cancerous tumor.

- **Link to YouTube Video:** 
- [https://youtu.be/FsKnxXuu9ps] - Watch a video which demonstrates how the Breast Cancer Disease Prediction application works.