li = ["apple", "cherry", 56.00, False, 34, 2, "john"] # ['apple', 'cherry', 56.0, False, 34, 2, 'john']
print(li)

li2 = ["banana", "banana"]
print(li2)  # ['banana', 'banana']  lists can have items with the same value

#list lenght

li3 = [14 , 56, 78, 78, 90, 32, 56, 7889]
print(len(li3)) # 8

#list indexing
li4 = ['a', 'b', 'c', 'd', 'e' ]
print(li4[0]) # 'a'
#print(li4[6])  # IndexError: list index out of range
print(li4[2]) # 'c'
print(li4[-1]) # 'e'
print(li4[-4:-1]) # ['b', 'c', 'd']

#list item data types
list1 = ["apple", "banana", "cherry"] #string
list2 = [1, 5, 7, 9, 3] #integer
list3 = [True, False, False] #boolean
list4= ["abc", 34, True, 40, "male"] #mixed data types
print(list1 , list2 , list3 , list4)

#type of list
thislist1 = [56, 71, 87, 69]
thislist2 = [ "grapes", "apple", "banana"]
thislist3 = [True, False, True]

print(type(thislist1), type(thislist2), type(thislist3))

thislist5 = ["apple", "banana", "cherry"]
if "apple" in thislist5:
  print("Yes, 'apple' is in the fruits list") #Yes, 'apple' is in the fruits list


