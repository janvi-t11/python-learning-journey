# Logical Operators in Python
a = 26 
b = 10 
print(a > 15 and b < 15) # True
print(a > b and b > a) # False
print(a > b or b  > a) # True
print(a < b or b < a) # False
print(not (a == b)) # True
print(not (a > b)) # False 

#truth table of "and" operator:
print(True and True)   # True
print(True and False)  # False
print(False and True)  # False
print(False and False) # False

#truth table of "or" operator:
print(True or True)   # True
print(True or False)  # True
print(False or True)  # True
print(False or False) # False

#truth table of "not" operator:
print(not True)  # False
print(not False) # True
