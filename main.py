import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading model

diabetes_disease_model = pickle.load(open("diabetes_model.sav", "rb"))

#heart_disease_model = pickle.load(open("C:/Users/gouri.mohite/PycharmProjects/Ml_Model_deployment/saved models/heart_disease_model.sav", "rb"))

parkinsons_model = pickle.load(open("parkinsons_model.sav", "rb"))

# sidebar for navigation
with st.sidebar:
    selected = option_menu("Multiple Disease Prediction System",

                           ["Diabetes Prediction",
                            #"Heart diseases Prediction",
                            "Parkinsons Prediction"],

                           icons=['activity', 'person'],
                           default_index=0)

# Diabetes prediction page
if selected == "Diabetes Prediction":
    # page title
    st.title("Diabetes Prediction Using ML")

    # getting the input from the user
    # columns for input field
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure')
    with col1:
        SkinThickness = st.text_input('Skin Thickness')
    with col2:
        Insulin = st.text_input('Insulin')
    with col3:
        BMI = st.text_input('BMI')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')
    with col2:
        Age = st.text_input('Age')

    # code for Prediction
    diab_dignosis = ""

    # Creating a button for Prediction

    if st.button("Diabetes Test Result"):
        diab_prediction = diabetes_disease_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if diab_prediction[0] == 1:
            diab_dignosis = "The Person is Diabetic"

        else:
            diab_dignosis = "The Person is Not Diabetic"

    st.success(diab_dignosis)





# if (selected=="Heart diseases Prediction"):
#     # page title
#     st.title("Heart Diseases Prediction Using ML")
#
#     # getting the input from the user
#     # columns for input field
#     col1, col2, col3 = st.columns(3)
#
#     with col1:
#         age = st.text_input('Age')
#     with col2:
#         sex = st.text_input('Gender')
#     with col3:
#         cp = st.text_input('Chest Pain Type')
#     with col1:
#         trestbps = st.text_input('resting blood pressure')
#     with col2:
#         chol = st.text_input('Cholestoral')
#     with col3:
#         fbs = st.text_input('fasting blood sugar')
#     with col1:
#         restecg = st.text_input('resting electrocardiographic')
#     with col2:
#         thalach = st.text_input('maximum heart rate achieved')
#     with col3:
#         exang = st.text_input('exercise induced angina')
#     with col1:
#         oldpeak = st.text_input('oldpeak')
#     with col2:
#         slope = st.text_input('slope of peak exercise ST segment')
#     with col3:
#         ca = st.text_input('number of major vessels')
#     with col1:
#         thal = st.text_input('thal')
#
#     # code for Prediction
#     heart_dignosis = ""
#
#     # Creating a button for Prediction
#
#     if st.button("Heart Disease Test Result"):
#         heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
#
#         if heart_prediction[0] == 1:
#             heart_dignosis = "The Person Have Heart Disease"
#
#         else:
#             heart_dignosis = "The Person Don't Have Heart Disease"
#
#     st.success(heart_dignosis)






if selected == "Parkinsons Prediction":
    # page title
    st.title("Parkinsons Prediction Using ML")

    # getting the input from the user
    # columns for input field
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        Fo = st.text_input('MDVP_Fo(Hz)')
    with col2:
        Fhi = st.text_input('MDVP_Fhi(Hz)')
    with col3:
        Flo = st.text_input('MDVP_Flo(Hz)')
    with col4:
        Jitter_percent = st.text_input('MDVP_Jitter(%) ')
    with col5:
        Jitter_Abs = st.text_input('MDVP_Jitter(Abs)')
    with col1:
        RAP = st.text_input('MDVP_RAP')
    with col2:
        PPQ = st.text_input('MDVP_PPQ')
    with col3:
        DDP = st.text_input('Jitter_DDP')
    with col4:
        Shimmer = st.text_input('MDVP_Shimmer')
    with col5:
        Shimmer_db = st.text_input('MDVP_Shimmer(dB)')
    with col1:
        Shimmer_APQ3 = st.text_input('Shimmer_APQ3 ')
    with col2:
        Shimmer_APQ5 = st.text_input('Shimmer_APQ5')
    with col3:
        MDVP_APQ = st.text_input('MDVP_APQ')
    with col4:
        Shimmer_DDA = st.text_input('Shimmer_DDA')
    with col5:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('spread1')
    with col5:
        spread2 = st.text_input('spread2')
    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_dignosis = ""

    # Creating a button for Prediction

    if st.button("parkinsons Disease Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[Fo, Fhi, Flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_db, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])

        if parkinsons_prediction[0] == 1:
            parkinsons_dignosis = "The Person Have Parkinsons Disease"

        else:
            parkinsons_dignosis = "The Person Don't Have Parkinsons Disease"

    st.success(parkinsons_dignosis)
