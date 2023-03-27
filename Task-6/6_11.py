# Define a dictionary of information about three cities
cities = {
    'Lahore': {
        'country': 'Pakistan',
        'population': 13929286,
        'fact': 'Lahore is the 2nd most populous city in Pakistan'
    },
    'Karachi': {
        'country': 'Pakistan',
        'population': 8398748,
        'fact': 'Karachi is home to the Mazar e Quaid'
    },
    'Islamabad': {
        'country': 'Pakistan',
        'population': 2140526,
        'fact': 'Capital City'
    }
}

# Loop through the dictionary and print the information for each city
for city in cities:
    # Print the name of the city
    print(f"\n{city}:")
    # Print the information about the city
    print(f"\tCountry: {cities[city]['country']}")
    print(f"\tPopulation: {cities[city]['population']}")
    print(f"\tFact: {cities[city]['fact']}")

