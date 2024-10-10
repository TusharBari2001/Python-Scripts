import requests

# Define the base URL for your API
base_url = "Enter Path Here"
auth_token = "Enter Authorized Token Here"
# Function to get the list of users
def get_all_users(token):
    headers = {
        "Content-Type": "application/json",
        "x-access-token": token,
    }
    
    response = requests.get(f"{base_url}/all", headers=headers)
    
    if response.status_code == 200:
        return response.json()['data']  # Assuming the response is in JSON format
    else:
        print(f"Failed to retrieve users: {response.status_code} - {response.text}")
        return []

# Function to delete users by user ID
def delete_users(user_ids, token):
    headers = {
        "Content-Type": "application/json",
        "x-access-token": token,
    }

    for user_id in user_ids:
        response = requests.delete(f"{base_url}/{user_id}", headers=headers)
        if response.status_code == 204:  # Assuming 204 No Content indicates success
            print(f"User {user_id} deleted successfully.")
        else:
            print(f"Failed to delete user {user_id}: {response.status_code} - {response.text}")

# Main logic
def main():
    # Step 1: Get all users
    users = get_all_users(auth_token)
    
    # Step 2: Extract user IDs
    user_ids = [user['user_id'] for user in users if user['username'] != 'admin']  # Adjust based on the actual structure of the user data
    
    # Step 3: Delete the users
    if user_ids:
        delete_users(user_ids, auth_token)
    else:
        print("No users to delete.")

if __name__ == "__main__":
    main()
