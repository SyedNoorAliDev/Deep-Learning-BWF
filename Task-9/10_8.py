# Create cats.txt and write data to it
with open('cats.txt', 'w') as f:
    f.write('Fluffy\n')
    f.write('Mittens\n')
    f.write('Whiskers\n')

# Create dogs.txt and write data to it
with open('dogs.txt', 'w') as f:
    f.write('Fido\n')
    f.write('Rex\n')
    f.write('Buddy\n')

# Try to read both files
try:
    with open('cats.txt', 'r') as f:
        print(f.read())

    with open('dogs.txt', 'r') as f:
        print(f.read())

    with open('nonexistent.txt', 'r') as f:
        print(f.read())

except FileNotFoundError:
    print('One of the files is missing!')
