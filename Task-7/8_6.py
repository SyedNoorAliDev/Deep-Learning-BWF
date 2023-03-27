def city_country(city, country):
    """Return a formatted string of city and country."""
    return f"{city.title()}, {country.title()}"

print(city_country('santiago', 'chile'))
print(city_country('new york', 'united states'))
print(city_country('sydney', 'australia'))
