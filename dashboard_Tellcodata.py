import streamlit as st
import pandas as pd
import multiapp as MultiApp
import os

#

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
        Useroverview = st.radio("Useroverview")
        userengagement= st.sidebar.selectbox(
            'Navigation',
            self.apps,
            format_func=lambda app: app['title'])

        app.run()
