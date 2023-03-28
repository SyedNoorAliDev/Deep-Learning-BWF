class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print("The restaurant is open.")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number


# Create an instance of the Restaurant class
restaurant = Restaurant("La Belle Vue", "French cuisine")
print(f"The restaurant has served {restaurant.number_served} customers.")
restaurant.number_served = 50
print(f"The restaurant has now served {restaurant.number_served} customers.")
restaurant.set_number_served(100)
print(f"The restaurant has now served {restaurant.number_served} customers.")
restaurant.increment_number_served(25)
print(f"The restaurant has now served {restaurant.number_served} customers.")
