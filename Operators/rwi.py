a = int(input("Enter your number1:")) #6
b = int(input("Enter your number2:")) #7
print(a+b) # 13
print(a-b) # -1
print(a/b) # 0.8571428571428571
print(a*b) # 42
print(a%b) # 6
print(a//b) # 0
print(a**b)# 279936

num = int(input("enter number:")) 
if num % 2 ==0:
    print("even")
else:
    print("odd")

p = 5000
r = 2
t = 7
si = p*r*t/100
print("simple interest is:", si)

num1 = int(input("enter number:"))
num2 = int(input("enter number:"))
if num1 > num2:
    print("num1 is grater than num2")
else:
    print("num2 is grater than num1")


a = int(input("enter number:"))
if a > 0:
    print("positive")
elif a < 0:
    print("negative")
else:
    print("0")


length = 15
breadth = 17
Area = length * breadth
print("area of rectangle is:", Area)
   
Year = int(input("enter year:"))
if Year%4 ==0:
    print("leap year")
else:
    print("not a leap year")


age = int(input("enter your age: "))
if age>=18 and age<=56:
    print("Eligible to party")
elif age<18:
    print("Not eligible to party")
else:
    print("Not eligible to party")


marks = int(input("Enter marks: "))

if marks >= 90:
    print("excellent")
elif marks >= 75:
        print("Distinction")
elif marks >= 35:
        print("Pass")
else:
    print("Fail")


marks = int(input("Enter marks: "))

if marks >= 35 or marks >= 90:
    print("Pass or excellent")
else:
    print("Fail")

