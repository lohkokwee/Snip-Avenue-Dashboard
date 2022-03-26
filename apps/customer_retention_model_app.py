import pandas as pd
import streamlit as st

def app():    
    data_overview = '''
        <h1>Customer Retention</h1>
        <p>Based on the data simulated, our team proposed a classification model based on logistic regression</p>
        <p>The dataframe below displays the information from the excel sheet.</p>
    '''
    st.markdown(data_overview, unsafe_allow_html=True)

    df = pd.read_csv("./assets/mock_dataset_cleaned.csv")
    st.write(df)