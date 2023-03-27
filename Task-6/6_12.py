users = {
    'aeinstein': {
        'first': 'Albert',
        'last': 'Einstein',
        'location': 'Princeton',
        'occupation': 'Theoretical physicist',
        'birth_year': 1879,
        'awards': ['Nobel Prize in Physics', 'Copley Medal'],
    },
    'mcurie': {
        'first': 'Marie',
        'last': 'Curie',
        'location': 'Paris',
        'occupation': 'Physicist and chemist',
        'birth_year': 1867,
        'awards': ['Nobel Prize in Physics', 'Nobel Prize in Chemistry'],
    },
}

for username in users:
    user_info = users[username]
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    occupation = user_info['occupation']
    birth_year = user_info['birth_year']
    awards = user_info['awards']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
    print("\tOccupation: " + occupation)
    print("\tBirth year: " + str(birth_year))
    print("\tAwards: ")
    for award in awards:
        print("\t\t- " + award)
