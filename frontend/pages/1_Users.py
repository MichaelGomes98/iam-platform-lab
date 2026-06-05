import streamlit as st
from data import users

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
        users["Status"] == status_filter
    ]

st.dataframe(filtered_users)