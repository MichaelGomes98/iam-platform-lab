import streamlit as st
#from data import users, audits, groups, active_users
import requests
import pandas as pd

st.set_page_config(
    page_title="IAM Platform Lab",
    page_icon="🔐",
    layout="wide"
)

st.title("🔐 IAM Platform Lab")

st.subheader("Dashboard")

users_response = requests.get(
    "http://127.0.0.1:8000/users"
)

groups_response = requests.get(
    "http://127.0.0.1:8000/groups"
)

audits_response = requests.get(
    "http://127.0.0.1:8000/audits"
)

users = pd.DataFrame(users_response.json())
groups = pd.DataFrame(groups_response.json())
audits = pd.DataFrame(audits_response.json())

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("All Users", len(users))

with col2:
    st.metric("Active Users", len(users[users["enabled"] == True]))

with col3:
    st.metric("Groups", len(groups))


with col4:
    st.metric("Audit Events", len(audits))