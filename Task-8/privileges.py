from UserClass import *
class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"Administrator Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, age, gender, occupation, email):
        super().__init__(first_name, last_name, age, gender, occupation, email)
        self.privileges = Privileges()

admin = Admin("John", "Doe", 30, "Male", "Administrator", "john.doe@example.com")
admin.privileges.show_privileges()
