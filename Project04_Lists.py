# @author Jungjae Lee
# Independent Study
# Created on June 12, 2022
# Sources: Lists by Colin Morris on the Kaggle
# --------------------------------------------------------------------------------


# --------------------------------------------------------------------------------
# ------------------------------------- Lists ------------------------------------
primes = [2, 3, 5, 7]
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K']
]

# A list can contain a mix of different types of variables
my_favorite_things = [32, 'raindrops on roses', help]


# --------------------------------------------------------------------------------
# ----------------------------------- Indexing -----------------------------------
print(planets[0])       # 'Mercury'
print(planets[1])       # 'Venus'
print(planets[-1])      # 'Neptune'
print(planets[-2])      # 'Uranus'


# --------------------------------------------------------------------------------
# ------------------------------------ Slicing -----------------------------------
print(planets[0:3])     # First three planets (Starting from index 0 and continuing up to but not including index 3):
                        # ['Mercury', 'Venus', 'Earth']
print(planets[:3])      # ['Mercury', 'Venus', 'Earth']
print(planets[3:])      # ['Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print(planets[1:-1])    # ['Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus']
print(planets[-3:])     # ['Saturn', 'Uranus', 'Neptune']
print(planets)


# --------------------------------------------------------------------------------
# -------------------------------- Changing Lists --------------------------------
planets[3] = 'Malacandra'
print(planets)          # ['Mercury', 'Venus', 'Earth', 'Malacandra', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
                        # It replaces index 3 ('Mars') to 'Malacandra'

planets[:3] = ['Mur', 'Vee', 'Ur']
print(planets)
planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars']


# --------------------------------------------------------------------------------
# -------------------------------- List Functions --------------------------------
# len function gives the length of a list
len(planets)        # How many planets are there? 8

# sorted function returns a sorted version of a list
sorted(planets)     # ['Earth', 'Jupiter', 'Mars', 'Mercury', 'Neptune', 'Saturn', 'Uranus', 'Venus']


# --------------------------------------------------------------------------------
# ------------------------------ Interlude: Objects ------------------------------
# imag function represent their imaginary part
x = 12
print(x.imag)
c = 12 + 3j
print(c.imag)
print(x.bit_length())


# --------------------------------------------------------------------------------
# --------------------------------- List Methods ---------------------------------
planets.append('Pluto')     # list.append modifies a list by adding an item to the end
print(planets)

planets.pop()               # list.pop removes and returns the last element of a list
print(planets)


# --------------------------------------------------------------------------------
# -------------------------------- Searching Lists -------------------------------
planets.index('Earth')

print("Earth" in planets)       # To check whether Earth is in the list
print("Calbefraques" in planets)

# If you would like to learn all the methods, use help(planets)


# --------------------------------------------------------------------------------
# ------------------------------------ Tuples ------------------------------------
# Tuples are almost exactly the same as lists. Often used for functions that have multiple return values.
# The differences are:
#   1. The syntax for creating them uses parentheses instead of square brackets.
#   2. They cannot be modified.

x = 0.125
print(x.as_integer_ratio())

numerator, denominator = x.as_integer_ratio()
print(numerator / denominator)


# Swapping two variables
a = 1
b = 0
a, b = b, a
print(a, b)