import streamlit as st
from data import audits

st.title("🔍 Audit")

st.dataframe(audits)