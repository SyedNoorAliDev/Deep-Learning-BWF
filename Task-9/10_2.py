# Open the file and read in each line
with open('learning_python.txt') as file_object:
    lines = file_object.readlines()

# Loop through each line and replace 'Python' with 'C'
for line in lines:
    new_line = line.replace('Python', 'C')
    print(new_line.strip())
