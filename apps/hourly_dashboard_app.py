# import math
# import pandas as pd
# import streamlit as st

# from components import common, bar

# def app():
#    hourly_intro = '''
#       <h1>Hourly Dashboard</h1>
#       <p style="text-align: justify">Comparing metrics based on our different service hours is important for many reasons. For instance, it could allow us to determine peaks and troughs in our service for us to be able to more efficiently allocate manpower. Select attributes from the dropdown to view the different metrics. To facilitate your comparison of the different metrics, we have also included an additional charting area at the bottom.
#       </p>
#    '''
#    st.markdown(hourly_intro, unsafe_allow_html = True)

#    df = pd.read_csv("./assets/mock_dataset_cleaned.csv")
#    cols = ['wait_time', 'queue_length', 'rating', 'price_paid']
#    col_dict = common.get_col_dict(cols)
#    cust_df = get_cust_df(df, cols)

#    user_col_1 = st.selectbox('Use the dropdown list to select a metric to compare against customer arrivals per hour.', [col for col in col_dict.keys()])
#    st.write(bar.get_bar(cust_df['arrival_time'], cust_df[col_dict[user_col_1]], "Hour (hr)", user_col_1))

#    user_col_2 = st.selectbox('Select a metric from the dropdown to compare multiple charts.', [None] + [col for col in col_dict.keys()])
#    if user_col_2 != None:
#       st.write(bar.get_bar(cust_df['arrival_time'], cust_df[col_dict[user_col_2]], "Hour (hr)", user_col_2))



# def get_cust_df(df, cols):
#    df['count'] = 1
#    df['arrival_time'] = df['arrival_time'].apply(lambda x: math.floor(x)) 
#    cust_df = df[cols + ['arrival_time', 'count']].groupby('arrival_time').sum().reset_index()

#    for col in cols:
#       cust_df[f"average_{col}"] = cust_df[col]/cust_df['count']
#       cust_df[f"average_{col}"] = cust_df[f"average_{col}"].round(2)
#       cust_df.drop(col, inplace = True, axis = 1)
      
#    return cust_df