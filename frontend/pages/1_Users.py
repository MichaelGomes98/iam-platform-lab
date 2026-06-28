import streamlit as st
import requests
import pandas as pd


# ==================================================
# API Configuration
# ==================================================

API_URL = "http://127.0.0.1:8000"


# ==================================================
# Retrieve users from backend API
# ==================================================

users_response = requests.get(
    f"{API_URL}/users"
)


if users_response.status_code == 200:

    users_data = users_response.json()

    users = pd.DataFrame(users_data)

else:

    st.error("Unable to retrieve users")
    st.stop()



# Retrieve groups from backend API

groups_response = requests.get(
    f"{API_URL}/groups"
)


if groups_response.status_code == 200:

    groups_data = groups_response.json()

else:

    st.error("Unable to retrieve groups")
    st.stop()



# ==================================================
# Page title
# ==================================================

st.title("👤 Users Management")



# ==================================================
# Create User
# ==================================================

with st.expander("➕ Create User"):


    first_name = st.text_input(
        "First Name"
    )


    last_name = st.text_input(
        "Last Name"
    )


    # Generate username automatically

    if first_name and last_name:

        username = (
            f"{first_name.lower()}."
            f"{last_name.lower()}"
        )

        st.info(
            f"Generated username: {username}"
        )


    if st.button(
        "Create User",
        key="create_user"
    ):


        if not first_name or not last_name:

            st.error(
                "First Name and Last Name are required"
            )


        else:


            new_user = {

                "username": username,
                "firstName": first_name,
                "lastName": last_name,
                "enabled": True

            }


            response = requests.post(

                f"{API_URL}/users",

                json=new_user

            )


            if response.status_code == 200:

                st.success(
                    "User created"
                )

                st.rerun()


            else:

                st.error(
                    "User creation failed"
                )



# ==================================================
# Enable / Disable User
# ==================================================

with st.expander("🔄 Enable / Disable User"):


    usernames = [

        user["username"]

        for user in users_data

    ]


    selected_user = st.selectbox(

        "Select User",

        usernames,

        key="enable_disable_user"

    )



    col1, col2 = st.columns(2)



    with col1:

        disable_clicked = st.button(

            "Disable User"

        )



    with col2:

        enable_clicked = st.button(

            "Enable User"

        )



    if disable_clicked:


        response = requests.put(

            f"{API_URL}/users/{selected_user}",

            json={
                "enabled": False
            }

        )


        if response.status_code == 200:

            st.success(
                "User disabled"
            )

            st.rerun()



    if enable_clicked:


        response = requests.put(

            f"{API_URL}/users/{selected_user}",

            json={
                "enabled": True
            }

        )


        if response.status_code == 200:

            st.success(
                "User enabled"
            )

            st.rerun()




# ==================================================
# Delete User
# ==================================================

with st.expander("🗑 Delete User"):


    selected_delete_user = st.selectbox(

        "Select User",

        usernames,

        key="delete_user"

    )



    if st.button(

        "Delete Selected User",

        key="delete_button"

    ):


        response = requests.delete(

            f"{API_URL}/users/{selected_delete_user}"

        )


        if response.status_code == 200:


            st.success(

                "User deleted"

            )

            st.rerun()


        else:


            st.error(

                "Unable to delete user"

            )




# ==================================================
# Assign User To Group
# ==================================================

with st.expander("👥 Assign User to Group"):



    group_names = [

        group["name"]

        for group in groups_data

    ]



    selected_assign_user = st.selectbox(

        "Select User",

        usernames,

        key="assign_user"

    )



    selected_assign_group = st.selectbox(

        "Select Group",

        group_names,

        key="assign_group"

    )



    if st.button(

        "Assign Group",

        key="assign_button"

    ):


        response = requests.put(

            f"{API_URL}/users/{selected_assign_user}/groups/{selected_assign_group}"

        )



        if response.status_code in [200,204]:


            st.success(

                "User assigned to group"

            )

            st.rerun()


        else:


            st.error(

                "Assignment failed"

            )




# ==================================================
# Remove User From Group
# ==================================================

with st.expander("➖ Remove User from Group"):



    selected_remove_user = st.selectbox(

        "Select User",

        usernames,

        key="remove_user"

    )



    selected_remove_group = st.selectbox(

        "Select Group",

        group_names,

        key="remove_group"

    )



    if st.button(

        "Remove Group",

        key="remove_button"

    ):


        response = requests.delete(

            f"{API_URL}/users/{selected_remove_user}/groups/{selected_remove_group}"

        )



        if response.status_code == 200:


            st.success(

                "User removed from group"

            )

            st.rerun()


        else:


            st.error(

                "Remove failed"

            )




# ==================================================
# Filter Users
# ==================================================

st.subheader("📋 User List")



status_filter = st.selectbox(

    "Filter by status",

    [
        "All",
        "Enabled",
        "Disabled"
    ],

    key="status_filter"

)



if status_filter == "Enabled":


    filtered_users = users[

        users["enabled"] == True

    ]



elif status_filter == "Disabled":


    filtered_users = users[

        users["enabled"] == False

    ]



else:


    filtered_users = users




# ==================================================
# Display Users Table
# ==================================================

st.dataframe(

    filtered_users,

    use_container_width=True

)