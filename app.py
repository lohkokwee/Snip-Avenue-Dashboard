import streamlit as st

from multiapp import MultiApp
from apps import home_app, service_dashboard_app, hourly_dashboard_app, geospatial_dashboard_app, customer_retention_model_app, data_info_app

app = MultiApp()

# Navigation
app.add_app("Home", home_app.app)
app.add_app("Service Dashboard", service_dashboard_app.app)
# app.add_app("Hourly Dashboard", hourly_dashboard_app.app)
app.add_app("Geospatial Dashboard", geospatial_dashboard_app.app)
app.add_app("Customer Retention Model", customer_retention_model_app.app)
app.add_app("Data Information", data_info_app.app)

# Main App
app.run()