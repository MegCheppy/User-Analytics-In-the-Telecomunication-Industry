import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Add a title and intro text
st.title('Tellco Data Analysis')
st.text('Analysis of customer data.')

# Create file uploader object
upload_file = st.file_uploader('Input Tellco Data')

# Check to see if a file has been uploaded
if upload_file is not None:
    # If it has then do the following:

    # Read the file to a dataframe using pandas
    df = pd.read_csv('Tellco_data.csv ')

    # Create a section for the dataframe statistics
    st.header('Statistics of Dataframe')
    st.write(df.describe())

    # Create a section for the dataframe header
    st.header('Header of Dataframe')
    st.write(df.head())

    # Create a section for matplotlib figure
    st.header('Plot of Data')
    
    fig, ax = plt.subplots(1,1)
    ax.scatter(x=df['Bearer Id'], y=df['Dur.'])
    ax.set_xlabel('Bearer Id')
    ax.set_ylabel('Dur.')
    
    st.pyplot(fig)