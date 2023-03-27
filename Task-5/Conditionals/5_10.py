current_users = ['alice', 'bob', 'charlie', 'david', 'eve']
new_users = ['frank', 'ALICE', 'george', 'hannah', 'david']

# convert all usernames in current_users to lowercase for case-insensitive comparison
current_users_lower = [user.lower() for user in current_users]

for user in new_users:
    # check if the username is already taken, ignoring case
    if user.lower() in current_users_lower:
        print(f"Sorry, the username '{user}' is not available. Please choose a new one.")
    else:
        print(f"The username '{user}' is available.")
