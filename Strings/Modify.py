#MODIFY STRINGS
#Strings are immutable, so we cannot change them directly. But we can create a new string with the desired modifications.
#uppercase 
# it makes all characters in the string uppercase
a = "John"
print(a.upper())# JOHN

#Lowercase 
# it makes all characters in the string lowercase
b = "Castel"
print(b.lower()) #castel

#replace string 
# it replaces a specified phrase with another specified phrase
c = "Bat"
print(c.replace("B", "C")) #Cat

#split string
#  it splits the string at the specified separator, and returns a list of substrings
d = "hello, i am john"
print(d.split(",")) #['hello', ' i am john']

#strip whitespace 
# it removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)
e=" hello world   "
print(e.strip()) #hello world

#find string 
# it finds the first occurrence of the specified value. It returns -1 if the value is not found
f="hello world"
print(f.find("world")) #6

#capitalize string 
# it converts the first character to upper case
x = "picture"
print(x.capitalize()) #Picture

#STRING END 
# isendswith() method returns True if the string ends with the specified value, otherwise False.
a = "JOHN"
print(a.endswith("HN")) #True
print(a.endswith("JO")) #False

#string count 
# it returns the number of times a specified value occurs in a string
y = "happiness"
print(y.count("s")) #2
print(y.count("p")) #2
print(y.count("e")) #0

#Escape Characters 
# in Python, escape characters are used to insert characters that are illegal in a string.
txt = "We are the so-called \"Vikings\" from the north."
print(txt)#We are the so-called "Vikings" from the north.

txt2 = 'It\'s a beautiful day.'
print(txt2)#It's a beautiful day.

txt3 = "hello\nworld"
print(txt3) #hello
             #world

#string formatting 
# it allows you to inject variables into strings
age = 25
txt= f"my name is john & i am {age} years old."
print(txt) #my name is john & i am 25 years old.