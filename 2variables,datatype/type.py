# type() function to know the datatype of variable
a = "John"
b = 36
c = 8.632
d = True
print(type(a)) #<class 'str'>
print(type(b)) #<class 'int'>
print(type(c)) #<class 'float'>
print(type(d)) #<class 'bool'>

#typecasting
x = 2
y = 3.5
z = "9"
print(float(x)) #2.0
print(str(y)) #'3.5'
print(int(z)) #9

#input() function to take user input
name = input("Enter your name: ")
print("Hello, " + name) #Hello, john

name = "John"
age = int(input("enter your age:"))
print(str(name) + " " + str(age)) #John 20