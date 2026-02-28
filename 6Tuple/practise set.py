#Write a program to count the number of zeros in the following tuple: 
a = (7, 0, 8, 0, 0, 9)
print(a.count(0)) #3

#Check that a tuple type cannot be changed in python.
a = (7, 0, 8, 0, 0, 9)
print(type(a)) #<class 'tuple'>

a = (7)
print(type(a)) #<class 'int'> because it is not a tuple, it is just an integer. To create a tuple with one element, you need to include a comma after the element.

#Find the index of 90.
a = (7, 0, 8, 90, 0, 9)
print(a.index(90)) #3

#Find the highest marks.
marks = (90, 80, 70, 60, 50)
print(max(marks)) #90

#Calculate total marks.
marks = (90, 80, 70, 60, 50)
print(sum(marks)) #350

#Create a tuple called fruits with the values
fruits = ("apple", "banana", "cherry")
print(fruits) # ('apple', 'banana', 'cherry')

#Print the second item in the tuple
print(fruits[1]) #banana

#Print the number of items using len()
print(len(fruits)) #3

#Unpack the tuple into three variables a, b, c
(a, b, c) = fruits 
print(a, b, c) #apple banana cherry

#Print the variable b
print(b) #banana

#make two tuples and join them 
a = (2, 2, 3)
b = (4, 5, 6)
c = a+b
print(c) # (2, 2, 3, 4, 5, 6)
