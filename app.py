from ast import Return
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly as plt
import re
import plotly.express as px
import seaborn as sns

import sys
sys.path.insert(0, '../scripts')



DATA_URL =('data/Tellco_data.csv')
 
def Loaddata(nrows):
    data=pd.read_csv(DATA_URL, nrows=nrows)
    return data

#sst.title('Tellco User Analytics')
st.subheader('Tellco Data')
st.write('tellco_data')
