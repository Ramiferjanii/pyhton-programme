# -----------------------
# -- Boolean Operators --
# -----------------------
# and
# or
# not
# -----------------------

age = 36
country = "tunis"
rank = 10

print(age > 16 and country == "tunis" and rank > 0)  # True
print(age > 16 and country == "KSA" and rank > 0)  # False

print(age > 40 or country == "tunis" or rank > 20)  # False
print(age > 40 or country == "Egypt" or rank > 20)  # True

print(age > 16)  # True
print(not age > 16)  # Not True = False