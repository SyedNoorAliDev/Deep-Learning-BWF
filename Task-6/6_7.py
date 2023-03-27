person = {
    'first_name': 'Ali',
    'last_name': 'Zar',
    'age': 30,
    'city': 'Islamabad',
}
person2 = {
    'first_name': 'Amna',
    'last_name': 'Ali',
    'age': 25,
    'city': 'Lahore',
}

person3 = {
    'first_name': 'Babar',
    'last_name': 'Jamshed',
    'age': 40,
    'city': 'Chile',
}
people = [person, person2, person3]
for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    age = person['age']
    city = person['city']
    print(f"{full_name.title()} is {age} years old and lives in {city}.")
