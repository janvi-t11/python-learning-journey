#Loop
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) #apple banana cherry 

  #loop
user = ["sam", "bill", "mark", "elon" ]
for i in user:
    print(i)


#Loop Through the Index Numbers
thislist2 = ["apple", "banana", "cherry"]
for i in range(len(thislist2)):
  print(thislist2[i]) #apple banana cherry 

box = ["pen", "pencil", "eraser"]
for i in range(len(box)):
    print(box[i])


#Using a While Loop
thislist3 = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist3):
  print(thislist3[i]) # apple banana cherry

#Looping Using List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist] # apple banana cherry

