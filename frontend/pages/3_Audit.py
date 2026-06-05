import streamlit as st
import requests
import pandas as pd

st.title("🔍 Audit")

response = requests.get(
    "http://127.0.0.1:8000/audits"
)

audits = pd.DataFrame(response.json())

st.dataframe(audits)