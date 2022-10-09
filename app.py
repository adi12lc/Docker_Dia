import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("SVC_class1.pkl","rb")
SVC_class=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Index Page"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Gender):
    
   
    prediction=SVC_class.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Gender]])
    print(prediction)
    return prediction


def main():
    st.title("Diabetes Prediction")
    html_temp = """
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Pregnancies = st.text_input("Pregnancies","")
    Glucose = st.text_input("Glucose","")
    BloodPressure = st.text_input("BloodPressure","")
    SkinThickness = st.text_input("SkinThickness","")
    Insulin = st.text_input("Insulin","")
    BMI = st.text_input("BMI","")
    DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction","")
    Age = st.text_input("Age","")
    intGender = st.selectbox('Gender',('Male', 'Female'))
    if intGender=='Male':
                Gender=1
    else:
                Gender=0		  		
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Gender)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    
    
    
