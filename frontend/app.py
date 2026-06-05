import streamlit as st

st.set_page_config(
    page_title="IAM Platform Lab",
    page_icon="🔐",
    layout="wide"
)

st.title("🔐 IAM Platform Lab")

st.markdown("### Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Users", "0", "Bonjour")

with col2:
    st.metric("Roles", "0")

with col3:
    st.metric("Groups", "0")

st.divider()

st.subheader("Actions")

st.button("Create User")
st.button("Disable User")
st.button("Assign Role")