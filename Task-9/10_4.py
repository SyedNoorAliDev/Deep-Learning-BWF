import datetime
while True:
    name = input("What is your name? ")
    print("Hello, " + name + "! Welcome to our site.")
    with open("guest_book.txt", "a") as file:
        file.write(name + " visited on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
