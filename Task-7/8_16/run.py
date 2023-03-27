# import the module and call the function
import greetings
greetings.greet("John")

# import only the function and call it directly
from greetings import greet
greet("Jane")

# import the function with an alias and call it using the alias
from greetings import greet as g
g("Jack")

# import the module with an alias and call the function using the alias
import greetings as g
g.greet("Jenny")

# import all functions from the module and call greet directly
from greetings import *
greet("Jim")
