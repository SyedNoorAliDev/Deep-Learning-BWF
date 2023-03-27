# Tests for equality and inequality with strings
name = "John"
print("Is name == 'John'? I predict True.")
print(name == "John")

print("Is name == 'Mary'? I predict False.")
print(name == "Mary")

# Tests using the lower() function
message = "Hello, World!"
print("Does the message contain 'world'? I predict True.")
print("world" in message.lower())

print("Does the message contain 'universe'? I predict False.")
print("universe" in message.lower())

# Numerical tests
age = 25
print("Is age == 25? I predict True.")
print(age == 25)

print("Is age != 25? I predict False.")
print(age != 25)

print("Is age > 18? I predict True.")
print(age > 18)

print("Is age < 30? I predict True.")
print(age < 30)

print("Is age >= 25? I predict True.")
print(age >= 25)

print("Is age <= 30? I predict True.")
print(age <= 30)

# Tests using the and keyword and the or keyword
x = 5
y = 10
z = 15
print("Is x < y and y < z? I predict True.")
print(x < y and y < z)

print("Is x < y or x > z? I predict True.")
print(x < y or x > z)

# Test whether an item is in a list
fruits = ["apple", "banana", "orange"]
print("Is 'banana' in fruits? I predict True.")
print("banana" in fruits)

print("Is 'pear' in fruits? I predict False.")
print("pear" in fruits)

# Test whether an item is not in a list
colors = ["red", "green", "blue"]
print("Is 'yellow' not in colors? I predict True.")
print("yellow" not in colors)

print("Is 'green' not in colors? I predict False.")
print("green" not in colors)

