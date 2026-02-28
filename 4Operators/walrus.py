# classic walrus eg
print(name := input("Enter name: "))




# Level 1 – Basic While Loop
# Write a program that:
# Keeps asking the user to enter a number. Stops when the user enters 0. Prints each number entered. Use the walrus operator

num = 1
while num > 0:
 print (num := int(input("enter number:" " ")))
else:
 print ("no input")
# wrong approach as loop condition was num > 0, but the requirement was to stop only when the user enters 0, so negative numbers would incorrectly end the loop.

while( num := int(input("enter number:" " "))) !=0:
 print(num)
#correct solution 

# Write a program that:
# Keeps asking the user to enter a word. Stops when the word is "quit". Prints only those words whose length is greater than 4
while (word := (input ("enter word: " " "))) != "quit":
    if len(word) > 4:
        print(word)


# Create a new list that stores: Only numbers greater than 5. But instead of storing the number, store its square. Use walrus operator inside list comprehension
numbers = [3, 8, 15, 2, 20, 7]
squares = [squares for x in numbers if x > 5 and (squares := x*x)]
print(squares)

