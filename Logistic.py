import streamlit as st
import joblib

def Logistic_model():
    model_path = "Logistic_Regresion_Titanic_21_03_2024.pkl"
    model = joblib.load(model_path)


    st.header("Enter Passenger Information:")
   
   

    slider1_key = 'slider1'
    slider2_key = 'slider2'
    slider3_key = 'slider3'
    slider4_key = 'slider4'
    selectbox1_key = 'selectbox1'
    selectbox2_key = 'selectbox2'
    selectbox3_key = 'selectbox3'
    
    # Get user input from Streamlit elements
    col1, col2 = st.columns(2)
    with col1:
        pclass = st.selectbox("Passenger Class:", [1, 2, 3],key=selectbox1_key)
        sex=1 if st.selectbox("Sex:", ["male", "female"], key=selectbox2_key) == "female" else 0
        age = st.slider("Age:", 0, 100, 30,key=slider1_key)
        sibsp = st.slider("Number of Siblings/Spouses Aboard:", 0, 8, 0,key=slider2_key)
    with col2:
        parch = st.slider("Number of Parents/Children Aboard:", 0, 6, 0,key=slider3_key)
        fare = st.slider("Fare:", 0, 600, 30,key=slider4_key)
        embarked = st.radio("Embarked From:", ["Cherbourg", "Queenstown", "Southampton"],key=selectbox3_key)
    

    # Feature dictionary
    feature_dict = {
        "Pclass": pclass,
        "Sex": sex,
        "Age": age,
        "SibSp": sibsp,
        "Parch": parch,
        "Fare": fare,
        "Embarked_C": 1 if embarked == "Cherbourg" else 0,
        "Embarked_Q": 1 if embarked == "Queenstown" else 0,
        "Embarked_S": 1 if embarked == "Southampton" else 0
    }

    if st.button("Predict Survival"):
        prediction = model.predict([list(feature_dict.values())])
        result = "Survived" if prediction[0] == 1 else "Not Survived"
        st.success(f"The passenger is predicted to have: {result}")

