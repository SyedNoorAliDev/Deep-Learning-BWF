while True:
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 + num2
        print("The result is:", result)
        break
    except ValueError:
        print("Please enter valid numbers!")
