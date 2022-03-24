import streamlit as st
import streamlit.components.v1 as components

def app():
    st.image("./assets/snips_avenue_logo.jpg")
    
    home_overview = '''
        <link rel="stylesheet" href="https://unicons.iconscout.com/release/v4.0.0/css/line.css">
        <h1>SNIPS AVENUE ANALYTICS DASHBOARD</h1> 
        <h2>About</h2>
        <p>This solution is works in tandem with the newly launched Snip Avenue application. Data is requested from our servers and displayed here. The goal of this dashboard is to inculcate a data-driven culture in the organisation, providing 
        key stakeholders with live information to drive decisions.</p>
    '''
    st.markdown(home_overview, unsafe_allow_html=True)

    home_navigation_guide = '''
        <h2>Navigation Assistance</h2>
        <p>The navigation panel to the left of the page grants you to access 3 different dashboards.</p>
        <li>Service Dashboard - view service related metrics (e.g. How long does an average haircut take?)</li>
        <li>Hourly Dashboard - view hourly metrics (e.g. What timeslots are the hottest?)</li>
        <li>Geospatial Dashboard - view location related information (e.g. Which outlets perform the best?)</li>
    '''
    st.markdown(home_navigation_guide, unsafe_allow_html=True)

    