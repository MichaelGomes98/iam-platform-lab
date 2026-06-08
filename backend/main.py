from fastapi import FastAPI
from dotenv import load_dotenv
import requests
import os

load_dotenv()
app = FastAPI()

def get_keycloak_token():
    data = {
        "grant_type" : "client_credentials",
        "client_id" : "iam-backend",
        "client_secret" : os.getenv("KEYCLOAK_CLIENT_SECRET")
    }
    url = "http://localhost:8081/realms/IAM-LAB/protocol/openid-connect/token"
    token_response = requests.post(
        url, 
        data = data)
    return token_response.json()["access_token"]

def get_keycloak_users():
    token = get_keycloak_token()
    url_users = "http://localhost:8081/admin/realms/IAM-LAB/users"
    headers = {
    "Authorization": f"Bearer {token}"
    }
    get_all_users = requests.get(url_users, headers=headers) 
    return get_all_users.json()

def filter_users_attributs():
    users = []
    all_users = get_keycloak_users()
    for user in all_users :
        {
        users.append(
        {
        "username": user["username"],
        "firstName": user["firstName"],
        "lastName": user["lastName"],
        "enabled": user["enabled"]
        }
        )
        },
    return users

def post_keycloak_create_users(new_user: dict):
    token = get_keycloak_token()

    url = "http://localhost:8081/admin/realms/IAM-LAB/users"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        url,
        headers=headers,
        json=new_user
    )

    print(response.status_code)
    print(response.text)

    return response


users = [
    {
        "username": "john.doe",
        "first_name": "John",
        "last_name": "Doe",
        "group": "Finance",
        "status": "Active"
    },
    {
        "username": "alice.smith",
        "first_name": "Alice",
        "last_name": "Smith",
        "group": "IT",
        "status": "Active"
    },
    {
        "username": "bob.test",
        "first_name": "Bob",
        "last_name": "Test",
        "group": "Marketing",
        "status": "Disabled"
    },
    {
        "username": "paul.durant",
        "first_name": "Paul",
        "last_name": "Durant",
        "group": "Finance",
        "status": "Active"
    }
]

groups = [
        {
        "group" : "IT",
        },
        {
        "group" : "Finance",
        },
        {
        "group" : "Marketing",
        },
        {
        "group" : "Security",
        }
    ]

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
        "action": "Assign Role",
        "made_by": "john.doe",
        "target": "alice.smith"
    },
    {
        "date": "01.06.2026",
        "action": "Create User",
        "made_by": "paul.durant",
        "target": "paul.durant"
    },
    {
        "date": "05.06.2026",
        "action": "Assign Role",
        "made_by": "john.doe",
        "target": "john.doe"
    }
]

@app.get("/")
def root():
    return {"message": "IAM Platform API"}

@app.get("/users")
def get_users():
    return filter_users_attributs()

@app.post("/users")
def create_user(user: dict):
    post_keycloak_create_users(user)
    return user

@app.get("/groups")
def get_groups():
    return groups

@app.post("/groups")
def create_group(group: dict):
    groups.append(group)
    return {
        "message": "Group created",
        "group": group
    }

@app.get("/audits")
def get_audits():
    return audits

@app.post("/audits")
def create_audit(audit: dict):
    audits.append(audit)
    return{
        "message" : "Audit created",
        "audit" : audit
    }

@app.delete("/users/{username}")
def delete_user(username: str):
    for user in users:
        if user["username"] == username:
            users.remove(user)

            return {
                "message": "User deleted"
            }

    return {
        "message": "User not found"
    }

@app.delete("/groups/{group_name}")
def delete_group(group_name: str):
    for group in groups:
        if group["group"] == group_name:
            groups.remove(group)
            return {
                "message": "Group deleted"
            }
    return {
        "message": "Group not found"
    }

@app.put("/users/{username}")
def update_user(username: str, updated_user: dict):
    for user in users:
        if user["username"] == username:
            user.update(updated_user)
            return {
                "message": "User updated",
                "user": user
            }
    return {
        "message": "User not found"
    }

@app.put("/groups/{group_name}")
def update_group(group_name: str, updated_group: dict):
    for group in groups:
        if group["group"] == group_name:
            group.update(updated_group)
            return {
                "message": "Group updated",
                "group": group
            }
    return {
        "message": "Group not found"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }