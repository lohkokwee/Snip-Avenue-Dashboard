import pandas as pd
import streamlit as st

from components import common, bar, line

'''
    Analytics:
    1. Sales by customer
    2. Sales by duration of service
    3. Sales by process duration
    4. Sales by location
'''

def app():
    service_intro = '''
        <h1>Service Dashboard</h1>
        <p>Service duration is the main metric which we will be comparing against in this dashboard. Service duration is an important factor to consider when evaluating service-based businesses. On its own, it gives us a gauge on how efficiently our company is performing. When it is compared against industry standards, it allows us to determine if our company is effectively meeting our target audience's requirements.
        </p>
    '''
    st.markdown(service_intro, unsafe_allow_html = True)

    service_slider = '''
        <h2>Service Interval Slider</h2>
        <p>The service interval slider configures the service duration into bins globally. This helps you compare different metrics that go alongside Snip Avenue's service duration.
        <p>
    ''' 
    st.markdown(service_slider, unsafe_allow_html = True)

    df = pd.read_csv("./assets/mock_dataset_cleaned.csv")
    col = "service_time"
    service_interval = st.slider("Use this slider to configure the service intervals.", 1, 10, 1)
    service_df = get_service_df(df, col, service_interval)

    service_histogram = '''
        <h2>Service Duration Histogram</h2>
        <p>Through the histogram, we can observe and make desicions and service optimisations based on the distributions of our service durations.</p>
    ''' 
    st.markdown(service_histogram, unsafe_allow_html = True)
    st.write(bar.get_bar(service_df['service_time_bins'], service_df['count'], 'Service Duration (in mins)', 'Quantity (customers)'))

    service_rating = '''
        <h2>Average Ratings</h2>
        <p>Within the same bins, we can compare the average ratings to help us determine consumer behaviour with respect to service durations.</p>
    ''' 
    st.markdown(service_rating, unsafe_allow_html = True)
    st.write(line.get_line(service_df['service_time_bins'], service_df['average_rating'], 'Service Duration (in mins)', 'Average Service Rating'))
    
    service_price = '''
        <h2>Average Price Paid</h2>
        <p>Finally, we can also compare also compare the different service durations against prices paid to determine if our service is resource efficient.</p>
    ''' 
    st.markdown(service_price, unsafe_allow_html = True)
    st.write(line.get_line(service_df['service_time_bins'], service_df['average_price'], 'Service Duration (in mins)', 'Average Price Paid'))


def get_service_df(df, col, service_interval):
    df = common.get_bins(df, col, service_interval)
    df['count'] = 1
    service_df = df[['service_time_bins', 'rating', 'price_paid', 'count']].groupby('service_time_bins').sum().reset_index()
    service_df['average_rating'] = service_df['rating']/service_df['count']
    service_df['average_rating'] = service_df['average_rating'].round(2)
    service_df['average_price'] = service_df['price_paid']/service_df['count']
    service_df['average_price'] = service_df['average_price'].round(2)

    return service_df