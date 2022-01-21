# Day Two of Python coding

# -------------------------- DATA STRUCTURES ------------------------------------------
# BUILT IN data structures within Python include lists, tuples, dictionaries, and sets


# LISTS ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
friends = ["Dani", "Beau", "Michelle", "Krista", "Shannon", "Charlie", "Charlie", "Simba"]
# index =    0        1        2          3          4          5         6          7

# the values in the list can be booleans and integers
luckyNum = [7, 13, 10, 28, 69, 49, 77, 99, 100]
# guide=    0   1   2   3   4   5   6   7   8

print(friends)

# remember index starts at zero
print(friends[0])

# put the square brackets [] to call a certain index
print(friends[2])

# use negatives to call from the back of the list, -1 or -2
print(friends[-1])

# use a colon to call all the indexes after as well
print(friends[3:])

# call another number after the colon to signify where in the list you want to stop
print(friends[2:6])
# IT WON'T RETURN THE NUMBER LISTED AFTER THE COLON, just the range in between

# LIST FUNCTIONS ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# example Lists
# friends = ["Dani", "Beau", "Michelle", "Krista", "Shannon", "Charlie", "Charlie", "Simba"]
# index =    0        1        2          3          4          5         6            7

# luckyNum = [7, 10, 13, 28, 49, 69, 77, 99, 100]
# index guide = 0   1   2   3   4   5   6   7   8

# EXTEND function allows you to append another list onto the end
# friends.extend(luckyNum)
# so now by including that function, when called it prints both lists
# print(friends)

# you can also reverse it, so you can decide what information gets printed first
# luckyNum.extend(friends)
# print(luckyNum)

# ****** Remember for list functions you need to call the LIST FIRST, then the function, then the print command*****

# APPEND allows you to add a value onto the end of the list
friends.append("Nara")
print(friends)

# INSERT lets you inject a value at a specific index in the list
friends.insert(4, "Joy")
# called^ index^    ^added value
print(friends)

# REMOVE allows you to remove a value from the list
friends.remove("Beau")
print(friends)

# CLEAR allows you to erase the whole list
# friends.clear()
# print(friends)

# POP removes the last element off the list
friends.pop()
print(friends)

# INDEX as a function lets you search for a value, and returns the index placement
print(friends.index("Joy"))
# ^ concatination ^ so you don't have to call twice

# if you INDEX a value not in the list it throws an error and tells you it's not in the list
# print(friends.index("Andrew"))

# COUNT functions searches for how many times the value submitted appears in the list
print(friends.count("Charlie"))

# SORT puts string lists in alphabetical order and numbers in ascending order
# print(friends)
# friends.sort()
# print(friends)

# print(luckyNum)
# luckyNum.sort()
# print(luckyNum)

# REVERSE won't sort the lists, but will print them backwards
print(friends)
friends.reverse()
print(friends)

print(luckyNum)
luckyNum.reverse()
print(luckyNum)

# COPY duplicates, so you could duplicate a list variable
friends2 = friends.copy()
print(friends2)

# TUPLES ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# very similar to lists, but with PARENTHESES and also immutable, can't be altered once set.

# common tuples include coordinates
# so this is a list with tuples inside, so the list can be altered but not the sets
coordinates = [(4, 5), (17, 10), (77, 44)]
# index guide=   0         1        2

print(coordinates[2])

# -------------------------- FUNCTIONS ------------------------------------------

# to tell python you want to use a function you use DEF and ():

def sayCheese():
    print("Everyone Smile!")
    # the syntax also includes a mandatory INDENTATION for everything included in the functi
# don't forget to call the function after defining it
sayCheese()

# inside the parentheses you can place a variable to define later
# BUT now you're bound to always defining it, you can't leave it empty
def sayHi(name):
    print("Hello " + name + "!")

sayHi("Kitty")
sayHi("Simba")

# you can also pass in TWO pieces of information/parameters

def sayHi(name, weight):
    print("Hello " + name + "!, you are " + weight + " kilos today.")

sayHi("Kitty", "5")
sayHi("Simba", "7")

# to change the weight to numbers/integers we have to apply STR() to the weight parameters so it can concatenate the two
def sayHi(name, weight):
    print("Hello " + name + "!, you are " + str(weight) + " kilos today.")

sayHi("Kitty", "500")
# and even though ^ we included one value as a string, it won't throw an error
sayHi("Simba", 700)

# RETURN STATEMENTS ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def raiseIt(num):
    print(num**3)
    #         ^ power operator symbol

raiseIt(4)
# since we aren't mixing strings and integers the numbers aren't a problem

#
def lunchSpecial(num):
    print(num**2)
    print("Order up!")

lunchSpecial(7)

# -------- RETURN & STORING IN A VARIABLE ----------------

def pizzaSpecial(num):
    return num*num*num
    print("Order up!")
    # ^ no code written after a RETURN STATEMENT will be run, notice this doesn't print

howMany = pizzaSpecial(2)
print(howMany)

# IF STATEMENTS ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

