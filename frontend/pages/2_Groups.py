import streamlit as st
import pandas as pd
from data import groups

st.title("👥 Groups")

if st.button("Create group"):
    st.success("Group created")
if st.button("Delete group"):
    st.success("Group deleted")


st.dataframe(groups)