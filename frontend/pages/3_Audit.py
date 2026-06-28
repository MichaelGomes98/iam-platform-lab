import streamlit as st
import requests
import pandas as pd


# ==================================================
# Page title
# ==================================================

st.title("🔍 Audit")



# ==================================================
# Retrieve audit logs
# ==================================================

response = requests.get(
    "http://127.0.0.1:8000/audits"
)



if response.status_code == 200:


    audits = pd.DataFrame(
        response.json()
    )


    st.dataframe(
        audits
    )


else:


    st.error(
        "Unable to retrieve audits"
    )