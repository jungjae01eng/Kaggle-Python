# @author Jungjae Lee
# Independent Study
# Created on June 13, 2022
# Sources: Strings and Dictionaries by Colin Morris on the Kaggle
# --------------------------------------------------------------------------------


# --------------------------------------------------------------------------------
# --------------------------------- String syntax --------------------------------
print("Pluto's a planet!")          # Use double quotations if it contains a single quote character
print('My does is named "Pluto"')   # Use single quotations if it contains a double quote character
print("\"Pluto\'s a planet!\"")     # If there are both single and double quote character, use "escaping" with backslash

# We can also use triple quote syntax for strings
triple_quoted_hello = """hello
world"""
print(triple_quoted_hello)


# --------------------------------------------------------------------------------
# ----------------------------- Strings are sequences ----------------------------
# Indexing
planet = 'Pluto'
print(planet[0])

# Slicing
print(planet[-3:])

# How long is this string?
print(len(planet))

# Can we loop over them?
print([char + '! ' for char in planet])


# --------------------------------------------------------------------------------
# -------------------------------- Strings Methods -------------------------------
# All caps
claim = "Pluto is a planet!"
print(claim)

print(claim.upper())

# All lowercase
print(claim.lower())

# Searching for the first index of a substring
print(claim.index('plan'))

print(claim.startswith('Pluto'))
print(claim.startswith(planet))
print(claim.endswith('planet'))     # False because of missing exclamation mark
print(claim.endswith('planet!'))


# --------------------------------------------------------------------------------
datestr = '1956-01-31'
year, month, day = datestr.split('-')
print(year)
print(month)
print(day)


date = '/'.join([month, day, year])
print(date)


# --------------------------------------------------------------------------------
# ----------------------------- Building strings with ----------------------------
print(planet + ', we miss you.')


# Whe calling any non-string object, we have to call str() on them first!
position = 9
print(planet + ", you'll always be the " + str(position) + "th planet to me.")


# To make a sentence neater
print("{}, you'll always be the {}th planet to me.".format(planet, position))


# --------------------------------------------------------------------------------
pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390

print1 = "{} weighs about {:.2} kilogram ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,
)

print(print1)


# --------------------------------------------------------------------------------
# --------------------------------- Dictionaries ---------------------------------
numbers = {'one' :1, 'two' :2, 'three' :3}      # 'one', 'two', and 'three' are the keys, and 1, 2, and 3 are their
                                                # corresponding values.

print(numbers['one'])

numbers['eleven'] = 11          # To add another key!
print(numbers)

numbers['one'] = 'Pluto'
print(numbers)                  # To change the value associated with an existing key


planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
print(planet_to_initial)


# --------------------------------------------------------------------------------
print('Saturn' in planet_to_initial)
print('Betelgeuse' in planet_to_initial)


print(numbers)
for k in numbers:
    print("{} = {}". format(k, numbers[k]))


' '.join(sorted(planet_to_initial.vallues()))


for planet, initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet.rjust(10), initial))