# Define the dictionary of favorite places
favorite_places = {
    'Ali': ['beach', 'mountains'],
    'Babar': ['city', 'park', 'museum'],
    'Chahar': ['coffee shop', 'bookstore']
}

# Loop through the dictionary and print each person's name and their favorite places
for person in favorite_places:
    # Create a string of the person's name and their favorite places
    places_str = ", ".join(favorite_places[person])
    print(f"{person}'s favorite places are: {places_str}.")
