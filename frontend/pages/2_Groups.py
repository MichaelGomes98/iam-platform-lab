import streamlit as st
import requests
import pandas as pd

# ==================================================
# Retrieve groups from FastAPI backend
# ==================================================

groups_response = requests.get(
    "http://127.0.0.1:8000/groups"
)

if groups_response.status_code == 200:

    groups = pd.DataFrame(
        [
            {
                "name": group["name"]
            }
            for group in groups_response.json()
        ]
    )

else:
    st.error("Unable to retrieve groups")

# ==================================================
# Page title
# ==================================================

st.title("👥 Groups")

# ==================================================
# Create Group
# ==================================================

with st.expander("Create Group"):

    group_name = st.text_input("Group Name")

    if st.button("Create Group"):

        if not group_name:
            st.error("Group name is required")

        else:

            new_group = {
                "group": group_name
            }

            create_group_response = requests.post(
                "http://127.0.0.1:8000/groups",
                json=new_group
            )

            if create_group_response.status_code == 200:
                st.success("Group created")
                st.rerun()

            else:
                st.error("Group creation failed")

# ==================================================
# Delete Group
# ==================================================

with st.expander("Delete Group"):

    all_groups = groups_response.json()

    group_names = [
        group["name"]
        for group in all_groups
]

    selected_group = st.selectbox(
        "Select Group",
        group_names,
        key="delete_group"
    )

    if st.button("Delete Group"):

        delete_group_response = requests.delete(
            f"http://127.0.0.1:8000/groups/{selected_group}"
        )

        if delete_group_response.status_code == 200:
            st.success("Group deleted")
            st.rerun()

        else:
            st.error("Unable to delete group")

# ==================================================
# Display groups table
# ==================================================

st.dataframe(groups)