# 1st method count
numbers = (1, 1, 1, 3, 4, 3, 6, 7, 6, 7, 8, 6, 7, 8 ,8)
print (numbers.count(3)) #2, because 3 appears 2 times in the tuple.
print(numbers.count(6)) # 3, because 6 appears 3 times in the tuple.

# 2nd method index
sweet = ("chocolate", "cakes", "lolipop", "jelly", "cakes")
print(sweet.index("cakes")) # 1, because "cakes" appears first at index 1 in the tuple.
print(sweet.index("jelly")) # 3, because "jelly" appears first at index 3 in the tuple.

"""Because tuples are immutable (cannot be changed after creation).
So methods that modify data like:

append()

remove()

pop()

extend()

insert()

are not available for tuples."""