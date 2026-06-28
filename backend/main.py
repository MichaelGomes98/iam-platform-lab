from fastapi import FastAPI
from dotenv import load_dotenv
import requests
import os


# ==================================================
# Application configuration
# ==================================================

load_dotenv()

app = FastAPI(
    title="IAM Platform API",
    description="Backend API connected to Keycloak",
    version="1.0"
)


# ==================================================
# Keycloak Configuration
# ==================================================

KEYCLOAK_URL = "http://localhost:8081"
REALM = "IAM-LAB"


# ==================================================
# Authentication - Get Keycloak Token
# ==================================================

def get_keycloak_token():

    data = {
        "grant_type": "client_credentials",
        "client_id": "iam-backend",
        "client_secret": os.getenv(
            "KEYCLOAK_CLIENT_SECRET"
        )
    }


    response = requests.post(
        f"{KEYCLOAK_URL}/realms/{REALM}/protocol/openid-connect/token",
        data=data
    )


    return response.json()["access_token"]



# ==================================================
# Keycloak Users Management
# ==================================================

def get_keycloak_users():

    token = get_keycloak_token()


    headers = {
        "Authorization": f"Bearer {token}"
    }


    response = requests.get(
        f"{KEYCLOAK_URL}/admin/realms/{REALM}/users?briefRepresentation=false",
        headers=headers
    )


    return response.json()



def create_keycloak_user(user):

    token = get_keycloak_token()


    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }


    return requests.post(
        f"{KEYCLOAK_URL}/admin/realms/{REALM}/users",
        headers=headers,
        json=user
    )



def update_keycloak_user(user_id, enabled):

    token = get_keycloak_token()


    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }


    return requests.put(
        f"{KEYCLOAK_URL}/admin/realms/{REALM}/users/{user_id}",
        headers=headers,
        json={
            "enabled": enabled
        }
    )



def delete_keycloak_user(user_id):

    token = get_keycloak_token()


    headers = {
        "Authorization": f"Bearer {token}"
    }


    return requests.delete(
        f"{KEYCLOAK_URL}/admin/realms/{REALM}/users/{user_id}",
        headers=headers
    )



# ==================================================
# Keycloak Groups Management
# ==================================================

def get_keycloak_groups():

    token = get_keycloak_token()


    headers = {
        "Authorization": f"Bearer {token}"
    }


    response = requests.get(
        f"{KEYCLOAK_URL}/admin/realms/{REALM}/groups",
        headers=headers
    )


    return response.json()



def create_keycloak_group(group):

    token = get_keycloak_token()


    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }


    return requests.post(
        f"{KEYCLOAK_URL}/admin/realms/{REALM}/groups",
        headers=headers,
        json={
            "name": group["group"]
        }
    )



def delete_keycloak_group(group_id):

    token = get_keycloak_token()


    headers = {
        "Authorization": f"Bearer {token}"
    }


    return requests.delete(
        f"{KEYCLOAK_URL}/admin/realms/{REALM}/groups/{group_id}",
        headers=headers
    )



# ==================================================
# User / Group relationship
# ==================================================

def get_user_groups(user_id):

    token = get_keycloak_token()


    headers = {
        "Authorization": f"Bearer {token}"
    }


    response = requests.get(
        f"{KEYCLOAK_URL}/admin/realms/{REALM}/users/{user_id}/groups",
        headers=headers
    )


    return [
        group["name"]
        for group in response.json()
    ]



def assign_user_group(user_id, group_id):

    token = get_keycloak_token()


    headers = {
        "Authorization": f"Bearer {token}"
    }


    return requests.put(
        f"{KEYCLOAK_URL}/admin/realms/{REALM}/users/{user_id}/groups/{group_id}",
        headers=headers
    )



def remove_user_group(user_id, group_id):

    token = get_keycloak_token()


    headers = {
        "Authorization": f"Bearer {token}"
    }


    return requests.delete(
        f"{KEYCLOAK_URL}/admin/realms/{REALM}/users/{user_id}/groups/{group_id}",
        headers=headers
    )



# ==================================================
# Formatting users for frontend
# ==================================================

def format_users():

    formatted_users = []


    for user in get_keycloak_users():

        groups = get_user_groups(
            user["id"]
        )


        formatted_users.append(
            {
                "username": user["username"],
                "firstName": user["firstName"],
                "lastName": user["lastName"],
                "enabled": user["enabled"],
                "groups": ", ".join(groups)
            }
        )


    return formatted_users


# ==================================================
# Audit Logs
# ==================================================

audits = [
    {
        "date": "04.06.2026",
        "action": "Create User",
        "made_by": "john.doe",
        "target": "alice.smith"
    },
    {
        "date": "02.06.2026",
        "action": "Delete User",
        "made_by": "alice.smith",
        "target": "alice.smith"
    },
    {
        "date": "28.05.2026",
        "action": "Assign User to Group",
        "made_by": "john.doe",
        "target": "alice.smith"
    }
]


@app.get("/audits")
def get_audits():

    return audits


# ==================================================
# API Endpoints
# ==================================================

@app.get("/")
def root():

    return {
        "message": "IAM Platform API"
    }



# ------------------------------
# Users
# ------------------------------

@app.get("/users")
def get_users():

    return format_users()



@app.post("/users")
def create_user(user: dict):

    response = create_keycloak_user(
        user
    )


    return {
        "status": response.status_code
    }



@app.put("/users/{username}")
def update_user(username: str, data: dict):

    for user in get_keycloak_users():

        if user["username"] == username:

            response = update_keycloak_user(
                user["id"],
                data["enabled"]
            )


            return {
                "status": response.status_code
            }


    return {
        "message": "User not found"
    }



@app.delete("/users/{username}")
def delete_user(username: str):

    for user in get_keycloak_users():

        if user["username"] == username:

            response = delete_keycloak_user(
                user["id"]
            )


            return {
                "status": response.status_code
            }



    return {
        "message": "User not found"
    }



# ------------------------------
# Groups
# ------------------------------

@app.get("/groups")
def get_groups():

    return get_keycloak_groups()



@app.post("/groups")
def create_group(group: dict):

    response = create_keycloak_group(
        group
    )


    return {
        "status": response.status_code
    }



@app.delete("/groups/{group_name}")
def delete_group(group_name: str):

    for group in get_keycloak_groups():

        if group["name"] == group_name:

            response = delete_keycloak_group(
                group["id"]
            )


            return {
                "status": response.status_code
            }



    return {
        "message": "Group not found"
    }



# ------------------------------
# Assign User to Group
# ------------------------------

@app.put("/users/{username}/groups/{group_name}")
def add_user_group(username, group_name):


    users = get_keycloak_users()
    groups = get_keycloak_groups()


    user_id = next(
        (
            u["id"]
            for u in users
            if u["username"] == username
        ),
        None
    )


    group_id = next(
        (
            g["id"]
            for g in groups
            if g["name"] == group_name
        ),
        None
    )


    if user_id and group_id:

        response = assign_user_group(
            user_id,
            group_id
        )


        return {
            "status": response.status_code
        }



    return {
        "message": "User or group not found"
    }



# ------------------------------
# Remove User from Group
# ------------------------------

@app.delete("/users/{username}/groups/{group_name}")
def remove_user_group_endpoint(username, group_name):


    users = get_keycloak_users()
    groups = get_keycloak_groups()


    user_id = next(
        (
            u["id"]
            for u in users
            if u["username"] == username
        ),
        None
    )


    group_id = next(
        (
            g["id"]
            for g in groups
            if g["name"] == group_name
        ),
        None
    )


    if user_id and group_id:


        response = remove_user_group(
            user_id,
            group_id
        )


        return {
            "status": response.status_code
        }


    return {
        "message": "User or group not found"
    }



# ------------------------------
# Health Check
# ------------------------------

@app.get("/health")
def health():

    return {
        "status": "healthy"
    }