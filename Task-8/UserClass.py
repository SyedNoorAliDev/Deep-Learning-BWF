class User:
    def __init__(self, first_name, last_name, age, gender, occupation, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.email = email
    
    def describe_user(self):
        print(f"User Profile:\nName: {self.first_name} {self.last_name}\nAge: {self.age}\nGender: {self.gender}\nOccupation: {self.occupation}\nEmail: {self.email}\n")
    
    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome to our platform.\n")

# Create some users
user1 = User("John", "Doe", 30, "Male", "Software Engineer", "john.doe@example.com")
user2 = User("Jane", "Smith", 25, "Female", "Graphic Designer", "jane.smith@example.com")
user3 = User("Bob", "Johnson", 40, "Male", "Sales Manager", "bob.johnson@example.com")

# Call the methods for each user
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
