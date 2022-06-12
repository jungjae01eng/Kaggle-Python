# @author Jungjae Lee
# Independent Study
# Created on June 8, 2022
# Last Updated on June 10, 2022
# Sources: Booleans and Conditionals by Colin Morris on the Kaggle
# --------------------------------------------------------------------------------


x = True
print(x)
print(type(x))      # boolean


# --------------------------------------------------------------------------------
# ----------------------------- Comparison Operations ----------------------------
# a == b    a equal to b
# a != b    a not equal to b
# a < b     a less than b
# a > b     a greater than b
# a <= b    a less than or equal to b
# a >= b    a greater than or equal to b


def can_run_for_president(age):
    """Can someone of the given age run for president in the US?"""
    # The US Constitution says you must be at least 35 years old
    return age >= 35


print("Can a 19-year-old run for president?", can_run_for_president(19))
print("Can a 45-year-old run for president?", can_run_for_president(45))


def is_odd(n):
    return(n % 2) == 1


print("Is 100 odd", is_odd(100))
print("Is -1 odd", is_odd(-1))


# --------------------------------------------------------------------------------
# ---------------------------- Combining Boolean Value ---------------------------
def can_run_for_president02(age, is_natural_born_citizen):
    """Can someone of the given age and citizenship status run for president in the US?"""
    # The US Constitution says you must be a natural-born citizen AND at least 35 years old
    return is_natural_born_citizen and (age >= 35)


print(can_run_for_president02(19, True))
print(can_run_for_president02(55, False))
print(can_run_for_president02(55, True))


# --------------------------------------------------------------------------------
# ------------------------------ Operator Precedence -----------------------------
# Lists are from the highest precedence(most binding) to the lowest precedence(least binding)
# (expressions), [expressions], {key: value}, {expressions}     => Binding or parenthesized expression, list display,
#                                                                   dictionary display, set display
# x[index], x[index:index], x(arguments), x.attribute           => Subscription, Slicing, call, attribute reference
# await x                                                       => Await expression
# **                                                            => Exponentiation
# +x, -x, ~x                                                    => positive, negative, bitwise NOT
# *, @, /, //, %                        => Multiplication, matrix multiplication, division, floor division, remainder
# +, -                                                          => Addition and subtraction
# <<, >>                                                        => Shifts
# &                                                             => Bitwise AND
# ^                                                             => Bitwise XOR
# |                                                             => Bitwise OR
# in, not in, is, is not, <, <=, >, >=, !=, ==                  => Comparisons (membership tests and identity test)
# not x                                                         => Boolean NOT
# and                                                           => Boolean AND
# or                                                            => Boolean OR
# if - else                                                     => Conditional expression
# lambda                                                        => Lambda expression
# :=                                                            => Assignment expression


# --------------------------------------------------------------------------------
# --------------------------------- Conditionals ---------------------------------
def inspect(x2):
    if x2 == 0:
        print(x2, "is zero")
    elif x2 > 0:
        print(x2, "is positive")
    elif x2 < 0:
        print(x2, "is negative")
    else:
        print(x2, "is unlike anything I've ever seen...")


inspect(0)
inspect(-15)


def f(x3):
    if x3 > 0:
        print("Only printed when x is positive; x =", x3)
        print("Also only printed when x is positive; x =", x3)
    print("Always printed, regardless of x's value; x =", x3)


f(1)
f(0)


# --------------------------------------------------------------------------------
# ------------------------------ Boolean Conversion ------------------------------
print(bool(1))          # All numbers are treated as true, except 0
print(bool(0))
print(bool("asf"))      # All strings are treated as true, except the empty string ""
print(bool(""))


if 0:
    print(0)
elif "spam":
    print("spam")
