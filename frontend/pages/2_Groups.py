import streamlit as st
import requests
import pandas as pd

st.title("👥 Groups")

if st.button("Create group"):
    st.success("Group created")
if st.button("Delete group"):
    st.success("Group deleted")

response = requests.get(
    "http://127.0.0.1:8000/groups"
)
groups = pd.DataFrame(response.json())


st.dataframe(groups)