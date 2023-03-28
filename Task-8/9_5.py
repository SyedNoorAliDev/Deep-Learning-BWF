class User:
    def __init__(self, first_name, last_name, age, gender, occupation, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.email = email
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"User Profile:\nName: {self.first_name} {self.last_name}\nAge: {self.age}\nGender: {self.gender}\nOccupation: {self.occupation}\nEmail: {self.email}\n")
    
    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome to our platform.\n")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

# Create an instance of the User class
user = User("John", "Doe", 30, "Male", "Engineer", "johndoe@example.com")

# Increment login_attempts several times and print the value
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Number of login attempts: {user.login_attempts}")

# Reset login_attempts and print the value again
user.reset_login_attempts()
print(f"Number of login attempts after reset: {user.login_attempts}")
