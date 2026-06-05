import streamlit as st
import requests
import pandas as pd

response = requests.get(
    "http://127.0.0.1:8000/users"
)

#st.write(response.status_code)
#st.write(response.json())

if response.status_code == 200:
    users = pd.DataFrame(response.json())
else:
    st.error("Unable to retrieve users")

st.title("👤 Users")

if st.button("Create User"):
    st.success("User creation requested")
if st.button("Disable User"):
    st.success("User disabled")
if st.button("Enable User"):
    st.success("User enabled")

status_filter = st.selectbox(
    "Filter by status",
    ["All", "Active", "Disabled"]
)

if status_filter == "All":
    filtered_users = users
else:
    filtered_users = users[
        users["status"] == status_filter
    ]

st.dataframe(filtered_users)
