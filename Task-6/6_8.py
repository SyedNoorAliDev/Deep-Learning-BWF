# Creating dictionaries for each pet
dog = {
    'animal': 'dog',
    'owner': 'Jalal',
}

cat = {
    'animal': 'cat',
    'owner': 'Ali',
}

bird = {
    'animal': 'bird',
    'owner': 'Babar',
}

# Storeing the dictionaries in a list called pets
pets = [dog, cat, bird]

# Looping through the list and print everything we know about each pet
for pet in pets:
    animal = pet['animal']
    owner = pet['owner']
    print(f"{animal.title()} owned by {owner.title()}")
