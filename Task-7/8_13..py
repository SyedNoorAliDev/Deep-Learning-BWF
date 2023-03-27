def build_profile(first, last, **user_info):
    """Build a user profile dictionary containing all given information."""
    profile = {'first_name': first, 'last_name': last}
    for key, value in user_info.items():
        profile[key] = value
    return profile

my_profile = build_profile('John', 'Doe', age=30, occupation='Software Engineer', hobby='Playing Guitar')
print(my_profile)
