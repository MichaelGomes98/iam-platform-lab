import streamlit as st
import requests
import pandas as pd

response = requests.get(
    "http://127.0.0.1:8000/users"
)

#st.write(response.status_code)
#st.write(response.json())

if response.status_code == 200:
    users = pd.DataFrame(response.json())
else:
    st.error("Unable to retrieve users")

st.title("👤 Users")

#User creation form
st.subheader("Create User")

with st.expander("Create User"):
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    group = st.selectbox(
        "Group",
        ["IT", "Finance", "Marketing", "Security"]
    )

    if first_name and last_name:
        username = f"{first_name.lower()}.{last_name.lower()}"
        st.info(f"Generated username: {username}")

    if st.button("Create User"):
        if not first_name or not last_name:
            st.error("First Name and Last Name are required")
        else:
            new_user = {
                "username": username,
                "first_name": first_name,
                "last_name": last_name,
                "group": group,
                "status": "Active"
            }
            response = requests.post(
                "http://127.0.0.1:8000/users",
                json=new_user
            )
            if response.status_code == 200:
                st.success("User created")
                st.rerun()
            else:
                st.error("User creation failed")


#User disable form
if st.button("Disable User"):
    st.success("User disabled")
if st.button("Enable User"):
    st.success("User enabled")

status_filter = st.selectbox(
    "Filter by status",
    ["All", "Active", "Disabled"]
)

if status_filter == "All":
    filtered_users = users
else:
    filtered_users = users[
        users["status"] == status_filter
    ]

st.dataframe(filtered_users)
