import streamlit as st
PAGE_TITLE = "Titanic Survival"
PAGE_ICON = "🚢"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
from Random import Ran_Fr_model
from Logistic import Logistic_model
from EDA import EDA_titanic
import streamlit.components.v1 as stc  # for running CSS and HTML in streamlit
from PIL import Image
import requests
from io import BytesIO
from Design import get_img_as_base64

get_img_as_base64("C:\\Users\\USER\\Desktop\\Streamlit\\Titanic\\Assets\\deep_blu.jpg")


html_temp= """
        <div style="background-color:#D33682; padding:10px; border-radius:10px;">
        <h1 style="color:white; text-align:center;"> Titanic Survival Prediction </h1>  
        <h4 style="color:pink; text-align:center;">By Victor Emuchay </h4>
        </div>
           """


def main():
       
   
    stc.html(html_temp)
    menu =["Home","EDA","ML","About"]
    
    choice=st.sidebar.selectbox("Menu",menu)
    
    if choice=="Home":
        st.write("<h2 style='text-align: left;'>Home</h2>", unsafe_allow_html=True)
        #st.write("<h3 style='text-align: left;'>Titanic Survival predictor App</h3>", unsafe_allow_html=True)
        st.write("<h4 style='text-align: center;'>Welcome to Titanic Survival Prediction Web App!</h4>", unsafe_allow_html=True)

        st.write(
        """
       
        Embark on a journey through history with our interactive Titanic Survival Prediction Web App. Step into the shoes of a 
        Titanic passenger and explore the factors that influenced survival on that fateful night in 1912.

        Using advanced machine learning techniques, our web app predicts the likelihood of survival based on passenger information 
        such as class, gender, age, family relations, fare, and port of embarkation. Simply input the details of a passenger, and 
        our model will provide you with an insightful prediction.

        Whether you're a history buff intrigued by the Titanic's story or a data enthusiast fascinated by predictive analytics, our
        user-friendly interface offers an engaging experience for all. Explore the Titanic Survival Prediction Web App today and 
        uncover the secrets of the past!
        ### Datasource
            -https://www.kaggle.com/datasets/yasserh/titanic-dataset""") 
        # Read the CSV file as bytes
        with open("C:\\Users\\USER\\Desktop\\Streamlit\\Titanic\\titanic.csv", "rb") as f:
            csv_data = f.read()

        # Create a download button for CSV data
        if st.button("Download CSV"):
            st.download_button(
            label="📊 Download Data",
            data=csv_data,
            file_name="titanic_data.csv",
            mime="text/csv")
        

        st.write(
            '''   
        ### App Content
            -EDA Section: Exploratory Data Analysis of Data
            -ML Section: ML Predictor App
          ''')
    elif choice=="EDA":
        EDA_titanic()
       
    elif choice=="ML":
        
        
        
        options =["Logistic Regression Model","Random Forest Model"]
        choice=st.sidebar.selectbox("Select Model",options)
        if choice=="Logistic Regression Model":
            st.progress(0.83)
            Logistic_model()
        elif choice=="Random Forest Model":
            st.progress(0.85)
            Ran_Fr_model()


            
    else:
        st.subheader("About Titanic Survival Prediction Web App")
        st.text("""

Welcome to the Titanic Survival Prediction Web App! This application is designed to predict the likelihood of survival for passengers aboard the Titanic based on various input features. 

The tragic sinking of the Titanic in 1912 remains a significant event in history, and this project utilizes machine learning techniques to analyze factors such as passenger class, sex, age, family relationships, fare, and port of embarkation to predict survival outcomes.

Our user-friendly interface allows you to input information about a passenger and receive an instant prediction regarding their survival. With the integration of the `joblib` library, we load a pre-trained machine learning model to provide accurate predictions.

Whether you're a history enthusiast curious about the fate of Titanic passengers or simply interested in exploring machine learning applications, our web app offers an engaging and informative experience.

Explore the Titanic Survival Prediction Web App and discover the intriguing insights it has to offer!""")
        











#with st.expander("Titanic"):

#   url = 'https://th.bing.com/th/id/OIP.Yg8TWBjS7QHwh5GKjltZrAHaHa?pid=ImgDet&w=208&h=208&c=7&dpr=1.5'
#    response = requests.get(url)
#    img = Image.open(BytesIO(response.content))

# Display image using Streamlit
#st.image(img, caption='Image from URL', use_column_width=True)

if __name__== '__main__':

    main()
