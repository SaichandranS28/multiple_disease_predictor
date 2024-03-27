# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 23:32:02 2024

@author: ssaic
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models

breast_cancer_model = pickle.load(open('C:/Users/ssaic/Desktop/Colab/breast_cancer_model.sav','rb'))
heart_disease_model = pickle.load(open('C:/Users/ssaic/Desktop/Colab/heart_disease_model.sav','rb'))
diabetes_model = pickle.load(open('C:/Users/ssaic/Desktop/Colab/diabetes_model.sav','rb'))


# sidebar to navigate

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction',
                           
                           ['Diabetes',
                            'Heart Disease',
                            'Breast Cancer'],
                           
                           icons = ['gender-female','heart','activity'],
                           
                           default_index = 0)
    
# Diabetes prediction page
if(selected == 'Diabetes'):
    
    st.title('Diabetes Prediction')
    st.image('C:/Users/ssaic/Desktop/Colab/Diabetes-Overview-1-768x768.png')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of times pregnant',value = "1")
        SkinThickness = st.text_input('Triceps skin fold thickness (mm)',value = "23")
        DiabetesPedigreeFunction = st.text_input('Diabetes pedigree function',value = "0.167") 


    with col2:
        Glucose = st.text_input('Plasma glucose concentration',value = "89")
        Insulin = st.text_input('2-Hour serum insulin (mu U/ml)',value = "94")
        Age = st.text_input('Age (years)',value = "21")    


    with col3:
        BloodPressure = st.text_input(' Diastolic blood pressure (mm Hg)',value = "66") 
        BMI = st.text_input('Body mass index',value = "28.1")


        
    
    
    #code for prediction
    diab_diagnosis = ''
    
    # Creating button for Prediction
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if(diab_prediction[0]==1):
            diab_diagnosis = 'The Person is Diabetic'
        else:
            diab_diagnosis = 'The Person is Not Diabetic'
    
    
        st.success(diab_diagnosis)
        st.balloons()
        text_contents = ("Here is your test results\n"+diab_diagnosis+"\nThanks for using Diabetes Predictor Page \n Created : S Saichandran")
        st.download_button('Download', text_contents)

if(selected == 'Heart Disease'):

    st.title('Heart Disease Prediction')
    st.image('C:/Users/ssaic/Desktop/Colab/heart-disease-hub.jpg')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age',value = "37")
        trestbps = st.text_input('Resting Blood Pressure',value = "130")
        restecg = st.text_input('Resting Electrocardiographic Results',value = "1")
        oldpeak = st.text_input('ST depression induced by exercise relative to rest',value = "3.5")
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect ',value = "2")


        
    with col2:
        sex = st.text_input('Sex',value = "1")
        chol = st.text_input('Serum Cholestoral',value = "250")
        thalach = st.text_input('Maximum Heart Rate achieved',value = "187")
        slope = st.text_input('the slope of the peak exercise ST segment',value = "0")

        
    with col3:    
        cp = st.text_input('Chest pain type',value = "2")
        fbs = st.text_input('Fasting Blood Sugar',value = "0")
        exang = st.text_input('Exercise Induced Angina',value = "0")
        ca = st.text_input('number of major vessels (0-3) colored by flourosopy',value = "0")
    
    #code for prediction
    heart_diagnosis = ''
    
    # Creating button for Prediction
    if st.button('Heart Disease Test Result'):
        
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        
        user_input = [float(x) for x in user_input]
        
        heart_disease_prediction = heart_disease_model.predict([user_input])
        
        if(heart_disease_prediction[0]==1):
            heart_diagnosis = 'The Person have Heart Disease'
        else:
            heart_diagnosis = 'The Person does Not have Heart Disease'
            
        st.balloons()
        st.success(heart_diagnosis)    
        text_contents = ("Here is your test results\n"+heart_diagnosis+"\nThanks for using Heart Disease Predictor Page \n Created : S Saichandran")
        st.download_button('Click to Download Result', text_contents)


if(selected == 'Breast Cancer'):
    
    #page title
    st.title('Breast Cancer Prediction')
    st.image('C:/Users/ssaic/Desktop/Colab/wf959478facebook1200x6303.jpg')
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        mean_radius = st.text_input('Mean Radius',value="13.54")
        mean_smoothness = st.text_input('Mean Smoothness',value="0.09779")
        mean_symmetry = st.text_input('Mean Symmetry',value = "0.1885")
        perimeter_error = st.text_input('perimeter Error',value = "2.058")
        concavity_error = st.text_input('Concavity Error',value = "0.02387")
        worst_radius = st.text_input('Worst Radius',value = "15.11")
        worst_smoothness = st.text_input('Worst Smoothness',value = "0.144")
        worst_symmetry = st.text_input('Worst Symmetry',value = "0.2977")
            
    with col2:
        mean_texture = st.text_input('Mean Texture',value = "10.38")
        mean_compactness = st.text_input('Mean Compactness',value = "0.08129")
        mean_fractal_dimension = st.text_input('Mean Fractal Dimension',value = "0.05766")
        area_error = st.text_input('Area Error',value = "23.56")
        concave_points_error = st.text_input('Concave Points Error',value = "0.01315")
        worst_texture = st.text_input('Worst Texture',value = "19.26")
        worst_compactness = st.text_input('Worst Compactness',value = "0.1773")  
        worst_fractal_dimension = st.text_input('Worst Fractal Dimension',value = "0.07259")
            
    with col3:
        mean_perimeter = st.text_input('Mean Perimeter',value = "87.46")
        mean_concavity = st.text_input('Mean Concavity',value = "0.06664")
        radius_error = st.text_input('Radius Error',value = "0.2699")
        smoothness_error = st.text_input('Smoothness Error',value = "0.008462")
        symmetry_error = st.text_input('Symmetry Error',value = "0.0198")
        worst_perimeter = st.text_input('Worst Perimeter',value = "99.7")
        worst_concavity = st.text_input('Worst Concavity',value = "0.239")
             
    with col4:    
        mean_area = st.text_input('Mean Area',value = "566.3")
        mean_concave_points = st.text_input('Mean Concavity Points',value = "0.04781")
        texture_error = st.text_input('Texture Error',value = "0.7886")
        compactness_error = st.text_input('Compactness Error',value = "0.0146")
        fractal_dimension_error = st.text_input('Fractal Dimension Error',value = "0.0023")    
        worst_area = st.text_input('Worst Area',value = "711.2")
        worst_concave_points = st.text_input('Worst Concave Points',value = "0.1288")
    
    
    #code for prediction
    breast_cancer_diagnosis = ''
    
    # Creating button for Prediction
    if st.button('Breast Cancer Test Result'):
        
        bc_user_input = [mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness,mean_compactness,mean_concavity,mean_concave_points,mean_symmetry,mean_fractal_dimension,radius_error,texture_error,perimeter_error,area_error,smoothness_error,compactness_error,concavity_error, concave_points_error, symmetry_error, fractal_dimension_error, worst_radius, worst_texture, worst_perimeter, worst_area, worst_smoothness, worst_compactness, worst_concavity, worst_concave_points, worst_symmetry, worst_fractal_dimension]
        bc_user_input = [float(x) for x in bc_user_input]
        breast_cancer_prediction = breast_cancer_model.predict([bc_user_input])
        
        if(breast_cancer_prediction[0]==1):
            breast_cancer_diagnosis = 'The Person have Breast Cancer'
        else:
            breast_cancer_diagnosis = 'The Person does Not have Breast Cancer'
            
        st.balloons()
        st.success(breast_cancer_diagnosis)
        text_contents = ("Here is your test results\n"+breast_cancer_diagnosis+"\nThanks for using Breast Cancer Predictor Page \n Created : S Saichandran")
        st.download_button('Click to Download Result', text_contents)