# @author Jungjae Lee
# Independent Study
# Created on June 6, 2022
# Sources: Hello, Python by Colin Morris on the Kaggle
# --------------------------------------------------------------------------------


spam_amount = 0                 # Variable assignment
print(spam_amount)              # Function calls

spam_amount = spam_amount + 4   # Reassigning the value of an existing variable

if spam_amount > 0:             # Conditionals, and ":" is the start of a new "code block"
    print("Spam is great!")     # Strings can be marked either by double or single quotation marks

viking_song = "Spam " * spam_amount     # Operator overloading: Can use "*" operator to repeat the string
print(viking_song)

type(spam_amount)       # integer
type(19.95)             # float: number with a decimal place


# --------------------------------------------------------------------------------
# ----------------------------------- Operator -----------------------------------
# a + b => Additional
# a - b => Subtraction
# a * b => Multiplication
# a / b => True division (Quotient of a and b)
# a // b => Floor division (Quotient of a and b, removing fractional parts)
# a % b => Modulus (Integer remainder after division of a by b
# a ** b => Exponentiation (a raised to the power of b)
# -a => Negation (The negative of a )

a = 5
b = 3

print(a / b)
print(a // b)
print(a ** b)


# --------------------------------------------------------------------------------
# ------------------ Builtin Functions for working with Numbers ------------------
print(min(1, 2, 3))
print(max(1, 2, 3))

print(abs(32))
print(abs(-32))

print(float(10))
print(int(3.33))
