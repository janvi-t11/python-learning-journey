tuple1 = (1, 5, 6, 7, 8, 97, 67)
print(tuple1) # (1, 5, 6, 7, 8, 97, 67)

tuple2 = ("john", "sam", "meet", "charlie")
print(type(tuple2)) # <class 'tuple'>

tuple3 = (1)
print(type(tuple3)) # <class 'int'>, because it is not a tuple, it is just an integer. To create a tuple with one element, you need to include a comma after the element.

tuple4 = (1,)
print(type(tuple4)) # <class 'tuple'>, because it is a tuple with one element. The comma is necessary to indicate that it is a tuple.

tuple5 = (14, "male", "true", 46.8, "john")
print(tuple5) # (14, 'male', 'true', 46.8, 'john') tuples can contain various types of datatypes.

tuple6 = (1, 5, 6, 7, 8, 97, 67)
print(len(tuple6)) # 7, the length of the tuple is 7 because it contains 7 elements.

tuple7 = (1, 5, 6, 7, 8, 97, 67)
print(tuple7[5]) # 97, because the index starts from 0, so the element at index 5 is 97.

tuple8 =("json", "React", "Node.js", "json")
print(tuple8) # ('json', 'React', 'Node.js', 'json') tuples can contain duplicate values, and they will be stored as they are.
 
tuple9 = ("Apple", "Banana", "Cherry")
print(tuple9[0:2]) # ('Apple', 'Banana') slicing the tuple from index 0 to index 1 (index 2 is not included).

tuple10 = ("BMW", "Audi", "Mercedes", "Honda", "Toyata")
print(tuple10[-1]) # 'Toyata', because the index starts from -1 for the last element, so the element at index -1 is 'Toyata'.
print(tuple10[-5:-1]) # ('BMW', 'Audi', 'Mercedes', 'Honda') slicing the tuple from index -5 to index -2 (index -1 is not included).
print(tuple10[0:]) # ('BMW', 'Audi', 'Mercedes', 'Honda', 'Toyata') slicing the tuple from index 0 to the end of the tuple.
print(tuple10[:4]) # ('BMW', 'Audi', 'Mercedes', 'Honda') slicing the tuple from the beginning to index 3 (index 4 is not included).
print(tuple10[:]) # ('BMW', 'Audi', 'Mercedes', 'Honda', 'Toyata') slicing the tuple from the beginning to the end of the tuple.
print(tuple10[::2]) # ('BMW', 'Mercedes', 'Toyata') slicing the tuple from the beginning to the end of the tuple with a step of 2, which means it will take every second element.

tuple11 = (91 , 92, 93, 94, 95)
if 96 in tuple11:
    print("yes, 96 is in the tuple")
else:
    print("no 96 is not in the tuple") # no 96 is not in the tuple, because 96 is not an element of the tuple.

    
    