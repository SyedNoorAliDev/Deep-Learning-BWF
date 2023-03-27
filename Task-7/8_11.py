def make_great(magicians):
    """Add 'the Great' to each magician's name in the list."""
    for i in range(len(magicians)):
        magicians[i] = "the Great " + magicians[i]
    return magicians

def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician)


magicians = ['Harry Houdini', 'David Blaine', 'Penn Jillette', 'Teller']

great_magicians = make_great(magicians[:])

print("\nOriginal magicians list:")
show_magicians(magicians)

print("\nGreat magicians list:")
show_magicians(great_magicians)
