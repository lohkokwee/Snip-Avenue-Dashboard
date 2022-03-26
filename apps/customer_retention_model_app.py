import pandas as pd
import streamlit as st

from components import common

def app():
    df = pd.read_csv("./assets/mock_dataset_cleaned.csv")
    
    customer_retention = '''
        <h1>Customer Retention</h1>
        <p style="text-align: justify">Based on the data simulated, our team proposed a classification model based on logistic regression to predict if a customer would become a repeat customer based on selected features.
         Randomness had been encoded when generating the class labels, to prevent an entirely deterministic model. This will then serve as a proof of concept that is ready to be utilised with actual data.</p>
        <p style="text-align: justify">Have a go at it! Choose your values for these selected variables to predict if a customer would stay with Snip Avenue.</p>
    '''
    st.markdown(customer_retention, unsafe_allow_html=True)

    st.header('Input Features')
    wait_time = st.slider(
        label='Wait Time',
        min_value=float(df['wait_time'].min()),
        max_value=float(df['wait_time'].max()),
        value=round(float(df['wait_time'].min()), 1),
        step=0.1)

    process_duration = st.slider(
        label='Process Duration',
        min_value=5.0,
        max_value=round(float(df['process_duration'].max()), 1),
        value=5.0,
        step=0.1)

    queue_length = st.slider(
        label='Queue Length',
        min_value=int(df['queue_length'].min()),
        max_value=int(df['queue_length'].max()),
        value=int(df['queue_length'].mean()),
        step=1)

    rating = st.slider(
        label='Rating',
        min_value=int(df['rating'].min()),
        max_value=int(df['rating'].max()),
        value=1,
        step=1)

    price_paid = st.slider(
        label='Price Paid',
        min_value=float(df['price_paid'].min()),
        max_value=float(df['price_paid'].max()),
        value=float(df['price_paid'].min()),
        step=0.1)

    user_variables = [wait_time, process_duration, queue_length, rating, price_paid]

    if st.button("Predict"):
        st.write(common.get_prediction(user_variables))