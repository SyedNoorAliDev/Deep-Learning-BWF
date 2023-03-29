filename = 'learning_python.txt'

# Reading the entire file
with open(filename) as file_object:
    contents = file_object.read()
print("***************************")
print(contents)

# Looping over the file object
with open(filename) as file_object:
    for line in file_object:
        print("***************************")
        print(line)

# Storing the lines in a list
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print("***************************")
    print(line)
