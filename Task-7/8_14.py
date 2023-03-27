def make_car(manufacturer, model, **car_info):
    """Build a dictionary containing information about a car."""
    car = {'manufacturer': manufacturer, 'model': model}
    for key, value in car_info.items():
        car[key] = value
    return car


car = make_car('subaru', 'outback', color='blue', package=True)
print(car)
