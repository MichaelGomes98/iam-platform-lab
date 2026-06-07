import streamlit as st
import requests
import pandas as pd

# Retrieve users from FastAPI backend
users_response = requests.get(
    "http://127.0.0.1:8000/users"
)

# Convert API response to DataFrame
if users_response.status_code == 200:
    users = pd.DataFrame(users_response.json())
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
# User disabled 
# ==================================================

with st.expander("Disable / Enable User"):

    all_users = users_response.json()

    usernames = [
        user["username"]
        for user in all_users
    ]

    selected_user = st.selectbox(
        "Select User",
        usernames
    )

    col1, col2 = st.columns(2)

    with col1:
        disable_clicked = st.button("Disable Selected User")

    with col2:
        enable_clicked = st.button("Enable Selected User")

    if disable_clicked:

        response = requests.put(
            f"http://127.0.0.1:8000/users/{selected_user}",
            json={"status": "Disabled"}
        )

        if response.status_code == 200:
            st.success("User disabled")
            st.rerun()

    if enable_clicked:

        response = requests.put(
            f"http://127.0.0.1:8000/users/{selected_user}",
            json={"status": "Active"}
        )

        if response.status_code == 200:
            st.success("User enabled")
            st.rerun()

# ==================================================
# User deleted 
# ==================================================

with st.expander("Delete User"):

    all_users_for_delete = users_response.json()

    usernames = [
        user["username"]
        for user in all_users_for_delete
    ]

    selected_user_to_delete = st.selectbox(
        "Select User",
        usernames,
        key="delete_user"
    )

    delete_clicked = st.button(
        "Delete Selected User"
    )

    if delete_clicked:

        response = requests.delete(
            f"http://127.0.0.1:8000/users/{selected_user_to_delete}"
        )

        if response.status_code == 200:
            st.success("User deleted")
            st.rerun()
        else:
            st.error("Unable to delete user")


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