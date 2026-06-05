from fastapi import FastAPI

app = FastAPI()

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
    return users

@app.get("/groups")
def get_groups():
    return groups

@app.get("/audits")
def get_audits():
    return audits