import pandas as pd

users = pd.DataFrame(
    {
        "Username": ["john.doe", "alice.smith", "bob.test", "paul.durant"],
        "First Name": ["John", "Alice", "Bob", "Paul"],
        "Last Name": ["Doe", "Smith", "Test", "Durant"],
        "Group": ["Finance", "IT", "Marketing", "Finance"],
        "Status": ["Active", "Active", "Disabled", "Active"],
    }
)

groups = pd.DataFrame(
    {
        "Groups": [
            "IT",
            "Finance",
            "Marketing",
            "Security"
        ]
    }
)

audits = pd.DataFrame(
    {
    "Date" : ["04.06.2026", "02.06.2026", "28.05.2026", "01.06.2026","05.06.2026"],
    "Action" : ["Create user", "Delete User", "Assign role", "Create User", "Asign role"],
    "Made by": ["john.doe", "alice.smith", "john.doe", "paul.durant", "john.doe"],
    "Target": ["alice.smith", "alice.smith", "alice.smith", "paul.durant", "john.doe"],   
    })

active_users = len(users[users["Status"] == "Active"])