from UserClass import User
class Admin(User):
    def __init__(self, first_name, last_name, age, gender, occupation, email):
        super().__init__(first_name, last_name, age, gender, occupation, email)
        self.privileges = ["can add post", "can delete post", "can ban user"]
    
    def show_privileges(self):
        print(f"Administrator Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")




admin = Admin("John", "Doe", 35, "Male", "Administrator", "johndoe@example.com")
admin.describe_user()
admin.show_privileges()

