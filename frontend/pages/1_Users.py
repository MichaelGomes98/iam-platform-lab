import streamlit as st
import requests
import pandas as pd

# Retrieve users from FastAPI backend
response = requests.get(
    "http://127.0.0.1:8000/users"
)

# Convert API response to DataFrame
if response.status_code == 200:
    users = pd.DataFrame(response.json())
else:
    st.error("Unable to retrieve users")

# Page title
st.title("👤 Users")

# ==================================================
# Create User
# ==================================================

st.subheader("Create User")

with st.expander("Create User"):

    # User information
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")

    # Available groups
    group = st.selectbox(
        "Group",
        ["IT", "Finance", "Marketing", "Security"]
    )

    # Generate username automatically
    if first_name and last_name:
        username = f"{first_name.lower()}.{last_name.lower()}"
        st.info(f"Generated username: {username}")

    # Submit user creation request
    if st.button("Create User"):

        # Validate mandatory fields
        if not first_name or not last_name:
            st.error("First Name and Last Name are required")

        else:
            # Build user
            new_user = {
                "username": username,
                "first_name": first_name,
                "last_name": last_name,
                "group": group,
                "status": "Active"
            }

            # Call FastAPI endpoint
            response = requests.post(
                "http://127.0.0.1:8000/users",
                json=new_user
            )

            # Display result
            if response.status_code == 200:
                st.success("User created")
                st.rerun()
            else:
                st.error("User creation failed")

# ==================================================
# User actions (In progress)
# ==================================================

if st.button("Disable User"):
    st.success("User disabled")

if st.button("Enable User"):
    st.success("User enabled")

# ==================================================
# User filtering
# ==================================================

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

# Display users table
st.dataframe(filtered_users)