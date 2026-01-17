# Arithmetic Operators in Python
a = 15
b = 5 

print(a + b) # Addition 20
print(a - b) # Subtraction 10
print(a * b) # Multiplication 75
print(a / b) # Division 3.0
print(a // b) # Floor Division 3
print(a % b) # Modulo 0
print (a ** b) # Power 759375

#comparison Operators in Python
a = 10 
b = 20

print(a == b) # Equal  (Answer:False)
print(a != b) # Not Equal (Answer:True)
print(a > b)  # Greater Than (Answer:False)
print(a < b)  # Less Than (Answer:True)
print(a>= b) # Greater Than or Equal to (Answer:False)
print(a <= b) # Less Than or Equal to (Answer:True)

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

# Assignment Operators in Python
a = 10 # Assign 10 to a (Answer:10)
print(a)
a +=5 # a = a + 5 (Answer:15)
print(a)
a -= 6 # a = a - 6 (Answer:9)
print(a)
a *= 5 # a = a * 5 (Answer:45)
print(a)
a /= 2 # a = a / 2 (Answer:22.5)
print(a)
a %= 3 # a = a % 3 (Answer:1.5)
print(a)
a **=5 # a = a ** 5 (Answer:7.59375)
print (a)
a //=4 # a = a // 4 (Answer:1.0)
print(a)

