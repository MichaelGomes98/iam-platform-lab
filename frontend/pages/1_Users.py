import streamlit as st
import pandas as pd

st.title("👤 Users")

if st.button("Create User"):
    st.success("User creation requested")

users = pd.DataFrame(
    {
        "Username": ["john.doe", "alice.smith", "bob.test"],
        "Status": ["Active", "Active", "Disabled"],
    }
)

st.dataframe(users)