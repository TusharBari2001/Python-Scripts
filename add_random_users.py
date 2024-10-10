import requests
import random
import string

# Define the endpoint URL
url = "path"

# Function to generate a random username
def generate_username(length=6):
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

# Function to create users and send POST requests
def add_users(num_users, token):
    roles = ["admin", "viewer"]
    headers = {
        # "Authorization": f"Bearer {token}",  # Replace with the correct authorization method if different
        "Content-Type": "application/json",
        "x-access-token": token,

    }

    for _ in range(num_users):
        username = generate_username()
        role = random.choice(roles)
        
        user_data = {
            "username": username,
            "enabled": True,
            "note": "",
            "role": role,
            "password": "1"
        }
        
        response = requests.put(url, json=user_data, headers=headers)
        
        if response.status_code == 201:
            print(f"User {username} with role {role} added successfully.")
        else:
            print(f"Failed to add user {username}: {response.status_code} - {response.text}")

# Replace 'your_token_here' with your actual token
auth_token = "Enter Authorized Token Here"

# Add 50 users
add_users(100, auth_token)
