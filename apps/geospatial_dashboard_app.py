import streamlit as st

import pandas as pd
import streamlit as st
from streamlit_folium import folium_static

from components import common, maps


'''
    Analytics:
    1. Sales by customer
    2. Sales by duration of service
    3. Sales by process duration
    4. Sales by location
'''

def app():
    geo_intro = '''
        <h1>Geospatial Dashboard</h1>
        <p>Coupled with data, heatmaps provides us with a concise birds eye view of any potential problems early at our various Snip Avenue outlets. Depending on the metric you selected, you would be able to view the "severities" of the different metrics at our shops in Singapore.
        </p>
    '''
    st.markdown(geo_intro, unsafe_allow_html = True)
    
    df = pd.read_csv("./assets/mock_dataset_cleaned.csv")
    cols = ['wait_time', 'process_duration', 'queue_length', 'rating', 'price_paid']
    map_df = get_map_df(df, cols)

    col_dict = common.get_col_dict(cols)
    user_col = st.selectbox('Use the dropdown list to select a metric to display the heatmaps by.', [col for col in col_dict.keys()])

    map_data = get_map_data(map_df, col_dict[user_col])
    fig = maps.get_map(map_data)
    folium_static(fig)

def get_map_df(df, cols):
    df['count'] = 1
    map_df = df[cols + ['postal_code', 'lat', 'long', 'count']].groupby(['postal_code', 'lat', 'long']).sum().reset_index()

    for col in cols:
        map_df[f"average_{col}"] = map_df[col]/map_df['count']
        map_df[f"average_{col}"] = map_df[f"average_{col}"].round(2)
        map_df.drop(col, inplace = True, axis = 1)

    return map_df

def get_map_data(df, user_col):
    df = df[['lat', 'long', user_col]]
    map_data = df.values.tolist()

    return map_data