import streamlit as st
import requests
import pandas as pd

# Retrieve groups from FastAPI backend
response = requests.get(
    "http://127.0.0.1:8000/groups"
)

if response.status_code == 200:
    groups = pd.DataFrame(response.json())
else:
    st.error("Unable to retrieve groups")

# Page title
st.title("👥 Groups")

# ==================================================
# Create User
# ==================================================

with st.expander("Create Group"):

    # User information
    group = st.text_input("Group name")

    if st.button("Create group"):
        if not group: 
            st.error("Group name is required")
        else: 
            new_group = {
                "group": group
            }
            response = requests.post(
                "http://127.0.0.1:8000/groups",
                json=new_group
            )

            # Display result
            if response.status_code == 200:
                st.success("Group created")
                st.rerun()
            else:
                st.error("Group creation failed")


# ==================================================
# Delete User (In progess)
# ==================================================       
if st.button("Delete group"):
    st.success("Group deleted")




st.dataframe(groups)