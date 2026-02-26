x = (1, 2, 3, 4, 5)
y = list(x) # converting the tuple to a list, because tuples are immutable, we cannot change their elements directly.
y[2] = 13 # changing the element at index 2 to 13, because lists are mutable, we can change their elements.
x = tuple(y) # converting the list back to a tuple, because we want to keep the original data structure as a tuple.
print(x) # (1, 2, 13, 4, 5) the updated tuple with the element at index 2 changed to 13.


x = ("crawl", "walk", "run")
y = list(x) # converting the tuple to a list, because tuples are immutable, we cannot change their elements directly.
y.append("jump") # adding the element "jump" to the end of the list, because lists are mutable, we can add elements to them.
x = tuple(y) # converting the list back to a tuple, because we want to keep the original data structure as a tuple.
print(x) # ('crawl', 'walk', 'run', 'jump') the updated tuple with the new element "jump" added to the end of the tuple.

x = ("red", "green", "blue")
y = ("purple", "orange")
x += y
print(x) # ('red', 'green', 'blue', 'purple', 'orange') the updated tuple with the elements of tuple y added to the end of tuple x. This is done using the += operator, which concatenates the two tuples together.

x = ("apple", "banana", "cherry")
y = list(x) # converting the tuple to a list, because tuples are immutable, we cannot change their elements directly.
y.remove("banana") # removing the element "banana" from the list, because lists are mutable, we can remove elements from them.
x = tuple(y)  
print(x) # ('apple', 'cherry') the updated tuple with the element "banana" removed from the tuple.

z = ("cat", "dog", "mouse")
del z
print(z) # NameError: name 'z' is not defined, because we have deleted the variable z, so it no longer exists in the memory.