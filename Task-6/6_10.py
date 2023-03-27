# Define a dictionary of favorite numbers for several people
favorite_numbers = {
    'Ali': [3, 7, 9],
    'Aneeq': [1, 2],
    'Haseeb': [8]
}

# Loop through the dictionary and print each person's name and their favorite numbers
for person in favorite_numbers:
    # Create a string of the person's name and their favorite numbers
    numbers_str = ", ".join(str(num) for num in favorite_numbers[person])
    print(f"{person}'s favorite numbers are: {numbers_str}.")
