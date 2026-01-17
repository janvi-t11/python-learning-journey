# first programm
print("hello world")
print("This will cause an error")  # result: SyntaxError: invalid syntax

# syntax IndentationError
if 5>2:
     print("five is greater than two")  #result no error

if 5>2:
 print("five is greater than two") # result IndentationError: expected an indented block

# Python Variables
 x=5
 y="hello"
 print(x , y)    # result:5 hello

 x=5
 y="hello" 
 print(x + y)   # result: TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Python Statements
 print("Python Is Fun") # Python Is Fun

# Many Statements 
 print("HI") #HI
 print("Hello") #Hello
 print("Welcome to Python Programming") #Welcome to Python Programming

# Semicolons are optional in Python. You can write multiple statements on one line by separating them with ; but this is rarely used because it makes it hard to read.
 print("hello") ;print("I'm") ;print("Janvi")

 print("Python is fun!") ;print("Really!") # SyntaxError: invalid syntax

 #Print Without a New Line
 print("hello" , end=" ")
 print("janvi") # hello janvi 

# print numbers
 print(5 + 2)
 print (8 * 9)
 print(16 / 2)
 print(3)
 print(358)
 print(50000)

# text  + number
 print("i am 20 currently")

# python variables
 A = "sally"
 B = 4
 print("A")
 print ("B") #result A B

 A = "sally"
 B = 4
 print(A)
 print (B)  #result sally 4
# The result changes because print("A") prints the literal string "A", while print(A) prints the value stored in variable A, which is "sally".

# casting
 print(str(3)) #result '3'
 print(int(3.0)) #result 3
 print(float(3)) #result 3.0


# Get the Type
# You can get the data type of a variable with the type() function.
 x="john"
 y=25.05
 print(type(x))  # <class 'str'>
 print(type(y))  # <class 'float'>

