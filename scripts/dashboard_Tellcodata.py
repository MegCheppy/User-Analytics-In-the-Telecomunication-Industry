from lib2to3.pgen2.pgen import DFAState
import streamlit as st
import pandas as pd
import altair as alt

from urllib.error import URLError


def get_Tellco_data():
        df = pd.read_csv(".data/Tellco_data.csv")
        BearerID= st.multiselect(
            "BearerID", list(df.index)
        )
        st.bar_chart.head()
       
        
        
#