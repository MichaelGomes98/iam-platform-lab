import streamlit as st

st.set_page_config(
    page_title="IAM Platform Lab",
    page_icon="🔐",
    layout="wide"
)

st.title("🔐 IAM Platform Lab")

st.subheader("Dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Users", "120")

with col2:
    st.metric("Roles", "15")

with col3:
    st.metric("Groups", "8")

with col4:
    st.metric("Applications", "25")