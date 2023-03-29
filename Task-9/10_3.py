name = input("Please enter your name: ")

with open("guest.txt", "w") as file:
    file.write(name)
