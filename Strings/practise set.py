# Write a python program to display a user entered name followed by Good Afternoon using input () function. 
name = str(input("enter your name:"))
print("Good Afternoon", name)

name = str(input("enter your name:"))
print(f"Good Afternoon {name}") #using f string formatting

#Write a program to detect double space in a string. 
string = str(input("enter a string:"))
if " " in string:
    print("double space found") #--- IGNORE --- hello  my  name is johnn 

 #Write a program to fill in a letter template given below with name and date.
letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|> 
''' 
print(letter .replace("<|Name|>,", "John").replace("<|Date|>" ,"29 october 2026"))


#Replace the double space from problem 3 with single spaces.
a = "Hello my name is john"
print(a.replace("  ", ""))

#Write a program to format the following letter using escape sequence characters.
letter = "Dear John,\n\tThis is a formatted letter.\nBest regards"
print(letter)