#string printing
print("hello, world") # hello, world
print('welcome to python programming') #welcome to python programming
print("""This is a multi-line string.
You can write across multiple lines.""") # This is a multi-line string. You can write across multiple lines.

# string concatenation
print("hello" + "world") # helloworld
print("hello" + " " + "world") # hello world

# string repetition
print("ha" * 3) # hahaha
print("na" * 5) # nanananana

#strings are array
a="JOHN"
print(a[3]) # N
print(a[0]) # J

#looping through a string
for x in "Coffee":
 print(x) # C o f f e e

#string length
a = "ten thousand"
print(len(a)) # 12


#checking a string
txt="You are not ordinary"
print("ordinary" in txt) #True

#using if in
txt="You are not ordinary"
if "ordinary" in txt:
 print("yes, 'ordinary' is present") # yes, 'ordinary' is present

# CHECKING NOT
txt="You are not ordinary"
print("extra" not in txt) #True

txt = "You are not ordinary"
if "extra" not in txt:
 print("yes, 'extra' is not present") # yes, 'extra' is not present
