# @author Jungjae Lee
# Independent Study
# Created on June 7, 2022
# Last Updated on June 11, 2022
# Sources: Functions and Getting Help by Colin Morris on the Kaggle
# --------------------------------------------------------------------------------


# --------------------------------------------------------------------------------
# ------------------------------ Defining Functions ------------------------------
def least_difference(a, b, c):
    """Return the smallest difference between any two numbers among a, b, and c.
    
    >>> least difference(1, 5, -5)
    4
    """     # Docstrings: This will show up when you use help() function.

    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)


print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7)
)


# --------------------------------------------------------------------------------
# ------------------------------- Default Arguments ------------------------------
print(1, 2, 3, sep=' < ')       # Can put some special string in between printed arguments using sep
print(1, 2, 3)


def greet(who="Colin"):
    print("Hello, ", who)


greet()
greet(who="Kaggle")
greet("world")


# --------------------------------------------------------------------------------
# ------------------------ Functions Applied to Functions ------------------------
def mult_by_five(x):
    return 5*x


def call(fn, arg):          # Here, "fn" is "mult_by_five (or 5)," and "arg" is "1"
    """Call fn on arg"""
    return fn(arg)          # Since fn is 5, and arg is 1, fn(arg) is 5


def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))      # fn(arg) is 5, so fn(fn(arg)) is 5*5 = 25


print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1),
    sep='\n',
)


# --------------------------------------------------------------------------------
def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5


print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),        # key argument returns the argument x that maximizes key(x)
    sep='\n',
)


# --------------------------------------------------------------------------------
# ----------------------------------- EXERCISE -----------------------------------
# Question 1
def round_to_two_places(num):
    """Return the given number rounded to two decimal places.
    """
    return round(num, 2)


print(round_to_two_places(3.25325))


# Question 2
round(3523405, -4)
