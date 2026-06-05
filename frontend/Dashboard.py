import streamlit as st
from data import users, audits, groups, active_users

st.set_page_config(
    page_title="IAM Platform Lab",
    page_icon="🔐",
    layout="wide"
)

st.title("🔐 IAM Platform Lab")

st.subheader("Dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("All Users", len(users))

with col2:
    st.metric("Active Users", active_users)

with col3:
    st.metric("Groups", len(groups))


with col4:
    st.metric("Audit Events", len(audits))