from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides
        
    def roll_die(self):
        print(randint(1, self.sides))

# create a 6-sided die and roll it 10 times
die6 = Die()
for i in range(10):
    die6.roll_die()

# create a 10-sided die and roll it 10 times
die10 = Die(sides=10)
for i in range(10):
    die10.roll_die()

# create a 20-sided die and roll it 10 times
die20 = Die(sides=20)
for i in range(10):
    die20.roll_die()
