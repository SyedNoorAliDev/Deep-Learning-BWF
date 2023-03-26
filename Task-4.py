#Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.
names = ["Ahmed","ANeeq","Ali"]
print(names[0],names[1],names[2])
#Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. The text of each message
#should be the same, but each message should be personalized with the person’s name.
for i in names:
    print ("Hi ",i)
# List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list
#to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”
trans = ["Car","bike","Cycle","Bus"]
for i in trans:
    print ("I would like to own a",i)
#If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to
#invite to dinner. Then use your list to print a message to each person, inviting them to dinner.
guests = ["Faraz","Haseeb","Husnain"]
for i in guests:
    print (i,", I would like to invite you to have dinner with me")
#You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of
#someone else to invite.
couldnt_make_it = guests.pop(0)
guests.append("Alti")
for i in guests:
    print (i,", I would like to invite you to have dinner with me")
print("Guests who didnt come: ",couldnt_make_it)
print("Invitation sent to: ",guests[len(guests)-1])
for i in guests:
    print (i,", I would like to invite you to have dinner with me")
#Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
guests.insert(0,"Shahzaib")
guests.insert(2,"Talal")
guests.append("Basit")
print("<<>>")
for i in guests:
    print (i,", I would like to invite you to have dinner with me")
#List: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
print("Only 2 guests can be accomodated now!!")
for i in range(4):
    print("Sorry",guests.pop(),"Couldnt invite you to the dinner!")
for i in guests:
    print (i,", You are still invited!!")
print(guests[0])
print(guests[1])
del guests[0]
del guests[0]
if (len(guests)==0):
    print("List is empty")
#Think of at least five places in the world you’d like to visit.
places = ["Netherlands","Switzerland","UK","US","India"]
print(places)
print(sorted(places))
print(places)
print(sorted(places,reverse=True))
print(places)
print(places.reverse())
print(places.reverse())
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)
#Guests: Working with one of the programs from Exercises 3-4 through 3-7, use len()
#to print a msg indicating the number of people you are inviting todinner.
guests = ["Faraz","Haseeb","Husnain"]
print("Number of people invited: ",len(guests))
#Function: Think of something you could store in a list. For example,you could make a list of mountains, rivers, countries, cities, languages, or any-
#thing else you’d like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.
cties = ["Lahore","Karachi","Islamabad","Peshawer","Quetta","Gilgit"]
cties.sort()
print(cties)
cties.sort(reverse=True)
print(cties)
cties.reverse()
print(cties)
print(sorted(cties))
print("number of cities: ",len(cties))
#Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
pizzas = ["Vegan","Fajita","Crust"]
for i in pizzas:
    print(i)
for i in pizzas:
    print("I like ",i," Pizza")
print("""Neapolitan pizza is known for its simplicity and features a thin crust with tomato sauce, fresh mozzarella cheese,
      and basil. This type of pizza is cooked quickly at a high temperature and has a slightly charred, crispy crust.""")
print("I really like pizza")
#Animals: Think of at least three different animals that have a common characteristic.
#Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
animals = ["Cat","rabbit","peacocks"]
for i in animals:
    print(i)
for i in animals:
    print("I love ",i)
print("Cat can be a great pet")
# Use a for loop to print the numbers from 1 to 20, inclusive.
for i in range(1,21):
    print (i)
#Make a list of the numbers from one to one million,
num_list = [i for i in range(1,1000001)]
#for i in num_list:
    #$print (i)
print("Max:",max(num_list))
print("Min:",min(num_list))
print(sum(num_list))
#Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.
odds = [i for i in range(1,21,2)]
for i in odds:
    print (i)
#Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.
multiples = [i for i in range(3,31,3)]
for i in multiples:
    print (i)
#Make a list of the first 10 cubes, and use a for loop to print out the value of each cube.
cubes = [i**3 for i in range(1,11)]
for i in cubes:
    print (i)
#Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
print("first three are:")
for i in foods[0:3]:
    print (i)
print("From middle of lists:")
for i in foods[2:]:
    print(i)
#Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas.
pizzas = ["Vegan","Fajita","Crust"]
friends_pizzas = pizzas[:]
pizzas.append("New pizza")
friends_pizzas.append("Pizza 1")
print("My Pizzas:-")
for i in pizzas:
    print (i)
print("Friend's Pizza")
for i in friends_pizzas:
    print(i)
#A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
tupley = ("Sanwich","Burger","Shawarma","Biryani","Karahi")
for i in tupley:
    print (i)
#Error: tupley[0] = 1
tupley = ("Pulao","Burger","Shawarma","Biryani","Pizza")
for i in tupley:
    print (i)
#All code complies with the PEP-80 standards


    






