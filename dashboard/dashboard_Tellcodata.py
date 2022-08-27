import streamlit as st
import pandas as pd
import multiapp as MultiApp
import os

os.chdir("dashboard")
os.listdir

def __init__(self):
        self.apps = []

def Useroverview():
        df = pd.read_csv("Field_Descriptions.csv")
        st.title('Tellco Data')
        st.dataframe(df)
       
        
def userengagement():
        st.title('User Engagement')  

def run(self):
        app=MultiApp()
        Useroverview = st.radio("User Overview Analysis")
        userengagement= st.sidebar.selectbox("User Engagement"
            'Navigation',
            self.apps,
            format_func=lambda app: app['title'])

        app.run['function']()
