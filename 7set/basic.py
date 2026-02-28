#set are unorderd & set does not contain duplicate values
kit = {"book", "bag", "pencil", "eraser", "shapner", "compass", "books"} 
print(kit) #{'pencil', 'shapner', 'books', 'bag', 'compass', 'eraser', 'book'}
print(type(kit)) #<class 'set'>
print(len(kit)) #7

#The values True and 1 is considered the same value in sets, and are treated as duplicates
switch = {True, 1, 2, 3, 4} #{True, 2, 3, 4}
print(switch)

#The values False and 0 are considered the same value in sets, and are treated as duplicates
switch = {False, 0 , 2, 3, 4} #{False, 2, 3, 4}
print(switch)

#set constructor ()
Fruits = set(("peach", "apple", "banana", "orange"))
print(Fruits) #{'orange', 'banana', 'peach', 'apple'}


