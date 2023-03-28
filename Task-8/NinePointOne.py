class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print("The restaurant is open.")

# Create an instance of the Restaurant class
restaurant = Restaurant("Pizza Place", "Italian")

# Print the two attributes individually
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Call both methods
restaurant.describe_restaurant()
restaurant.open_restaurant()

#9.2
restaurant1 = Restaurant("Pizza Hut", "Italian")
restaurant1.describe_restaurant()
restaurant2 = Restaurant("Broadway", "French")
restaurant1.describe_restaurant()
restaurant3 = Restaurant("Pizza Online", "Arab")
restaurant3.describe_restaurant()

