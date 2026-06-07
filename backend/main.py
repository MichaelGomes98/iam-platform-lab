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

@app.post("/users")
def create_user(user: dict):
    users.append(user)
    return {
        "message": "User created",
        "user": user
    }

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