import pandas as pd
import streamlit as st

def app():    
    data_overview = '''
        <h1>Data Information</h1>
        <p>The data that we used and presented was data that we generated through Microsoft Excel. We generated a total of 10,277 rows of datapoints, with each column having a set distribution. This was to mimic a real-life scenario dataset at Snip Avenue as much as possible.</p>
        <p>The dataframe below displays the information from the excel sheet.</p>
    '''
    st.markdown(data_overview, unsafe_allow_html=True)

    df = pd.read_csv("./assets/mock_dataset_cleaned.csv")
    st.write(df)