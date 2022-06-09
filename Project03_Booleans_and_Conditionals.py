# @author Jungjae Lee
# Independent Study
# Created on June 8, 2022
# Sources: Functions and Getting Help by Colin Morris on the Kaggle
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
    return(n%2) == 1


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
