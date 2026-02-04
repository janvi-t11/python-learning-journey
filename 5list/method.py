li1 = [1, 2, 3, 4, ]
li1.append(5)
print(li1) #[1, 2, 3, 4, 5] add an item to the end of the list

li1.extend([6, 7]) 
print(li1) #[1, 2, 3, 4, 5, 6, 7] To append elements from another list to the current list, use the extend() method.


thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) #['apple', 'banana', 'cherry', 'kiwi', 'orange']

thislist1 = ["apple", "banana", "cherry"]
thislist1.remove("banana")
print(thislist1) #['apple', 'cherry'] Remove "banana" from the list

thislist2 = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist2.remove("banana")
print(thislist2) # ["apple", "cherry", "banana", "kiwi"]  Remove the first occurrence of "banana":

thislist3 = ["apple", "banana", "cherry"]
thislist3.pop(1)
print(thislist3) # ['apple', 'cherry'] Remove the second item:

thislist4 = ["apple", "banana", "cherry"]
thislist4.pop()
print(thislist4) # ['apple', 'banana'] Remove the last item: If you do not specify the index, the pop() method removes the last item.

thislist5 = ["apple", "banana", "cherry"]
del thislist5[0]
print(thislist5) #['banana', 'cherry'] The del keyword also removes the specified index:

thislist6 = ["apple", "banana", "cherry"]
del thislist6 # The del keyword  delete the list completely.

thislist7 = ["apple", "banana", "cherry"]
thislist7.clear()
print(thislist7) #[]the clear() method empties the list the list still remains, but it has no content
