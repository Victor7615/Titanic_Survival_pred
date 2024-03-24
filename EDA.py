import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns


@st.cache_data         # for optimiztion and speed
def load_data(data):
    df=pd.read_csv(data)
    return df



def EDA_titanic():
    data=load_data("C:\\Users\\USER\\Desktop\\Streamlit\\Titanic\\cleaned_titanic.csv")
    data2=load_data("C:\\Users\\USER\\Desktop\\Streamlit\\Titanic\\titanic.csv")
    data.drop("Name",axis=1)
    
    submenu= st.sidebar.selectbox("SubMenu",["Describe","Visualization"])

    if submenu== "Describe":
        st.dataframe(data)
        
        with st.expander("Data Type Summary"):
            
            st.dataframe(data.dtypes)
        
        with st.expander("Descriptive Summary"):
            st.dataframe(data.describe())
    else:
        st.write("<h2 style='text-align: center;'>Visualization</h2>", unsafe_allow_html=True)

        numeric_data = data.select_dtypes(include=['number'])
        corr_matrix = numeric_data.corr()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.figure(figsize=(12, 10))

        # Display correlation matrix heatmap
       
        st.write("<h3 style='text-align: center;'>Correlation Matrix</h3>", unsafe_allow_html=True)
        sns.heatmap(corr_matrix, annot=corr_matrix.values, fmt=".2f", cmap="coolwarm", square=True)
        st.pyplot()

        
        st.write("<h3 style='text-align: center;'>Distribution of Age</h3>", unsafe_allow_html=True)
        sns.histplot(data['Age'],kde=True,bins=15)
        st.pyplot()

       
        st.write("<h3 style='text-align: center;'>Barplot of Gender Survival</h3>", unsafe_allow_html=True)

        sns.barplot(x="Sex",y="Survived",data=data2,palette="YlGnBu",estimator=sum)
        st.pyplot()

        st.write("<h3 style='text-align: center;'>Barplot of Survival by Embarked From</h3>", unsafe_allow_html=True)

        sns.barplot(x="Embarked",y="Survived",data=data2,palette="YlGnBu",estimator=sum)
        st.pyplot() 

        st.write("<h3 style='text-align: center;'>Passager Class Survival</h3>", unsafe_allow_html=True)

        sns.barplot(x="class",y="Survived",data=data2,palette="YlGnBu",estimator=sum)
        st.pyplot() 