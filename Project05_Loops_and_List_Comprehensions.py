# @author Jungjae Lee
# Independent Study
# Created on June 12, 2022
# Sources: Lists by Colin Morris on the Kaggle
# --------------------------------------------------------------------------------


# --------------------------------------------------------------------------------
# ------------------------------------- Loops ------------------------------------
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:              # for (the variable name to use) in (the set of values to loop over)
    print(planet, end=' ')          # Print all on the same line
print(end="\n")

multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult        # 2*2*2*3*3*5
print(product)

x = 2*2*2*3*3*5
print(x)


# Print all the uppercase letters in s, one at a time.
s = 'seganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image,' \
    'Or video.'

for char in s:
    if char.isupper():
        print(char, end='')


# --------------------------------------------------------------------------------
# ------------------------------------ Range() -----------------------------------
for i in range(5):
    print("Doing important work. i =", i)       # Returns a sequence of numbers.


# --------------------------------------------------------------------------------
# ---------------------------------- while Loops ---------------------------------
i = 0
while i < 10:
    print(i, end='')
    i += 1      # increase the value of i by 1
print(end="\n")


# --------------------------------------------------------------------------------
# ------------------------------ List comprehensions -----------------------------
squares = [n**2 for n in range(10)]
print(squares)

# Same thing without a list comprehension:
squares = []
for n in range(10):
    squares.append(n**2)
print(squares)


print(planets)
short_planets = [planet for planet in planets if len(planet) < 6]
print(short_planets)


loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
print(loud_short_planets)


print([32 for planet in planets])


# --------------------------------------------------------------------------------
def count_negatives(nums):
    n_negative = 0
    for num in nums:
        if num < 0:
            n_negative = n_negative + 1
    return n_negative


print(count_negatives([5, -1, -2, 0, 3]))


# OR We can make it in one line
def count_negatives2(nums):
    return len([num for num in nums if num < 0])


print(count_negatives2([5, -1, -2, 0, 3]))


# We can actually minimize it more!
def count_negatives3(nums):
    return sum([num < 0 for num in nums])


print(count_negatives3([5, -1, -2, 0, 3]))

