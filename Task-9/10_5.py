# Open the file for appending
with open('programming_responses.txt', 'a') as file:
    # Ask for the first response
    response = input("Why do you like programming? (Press q to quit): ")

    # Loop until the user types 'q'
    while response != 'q':
        # Write the response to the file
        file.write(response + '\n')

        # Ask for the next response
        response = input("Why do you like programming? (Press q to quit): ")

print("Responses saved to programming_responses.txt")
