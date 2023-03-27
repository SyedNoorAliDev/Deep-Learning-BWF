def make_great(magicians):
    """Add 'the Great' to each magician's name in the list."""
    for i in range(len(magicians)):
        magicians[i] = "the Great " + magicians[i]

def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician)

magicians = ['Harry Houdini', 'David Blaine', 'Penn Jillette', 'Teller']

# modify the list
make_great(magicians)

# verify that the list has been modified
show_magicians(magicians)
