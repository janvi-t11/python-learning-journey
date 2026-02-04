#identity Operators in Python
x = [10,2,3]
y= [12 , 13, 14]
z= x

print(x is z) # True because z references to x
print (x is y) # False because x is not y
print(x is not y) # True because x is not y
print(x is not z) # False because z references to x


x = [7,8,9]
y = [7,8,9]
print(x == y) #is - Checks if both variables point to the same object in memory (true)
print (x is y) #== - Checks if the values of both variables are equal (false)