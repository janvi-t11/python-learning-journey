#The union() method returns a new set with all items from both sets.
num = {1, 2, 3, 4}
alpha = {"a", "b", "c", "d", "e"}
maths = num.union(alpha)
print(maths) #{1, 2, 3, 4, 'b', 'c', 'e', 'a', 'd'}

set1 = {23, 46, 87, 9, 0}
set2 = {82, 78, 90}
set3 = set1 | set2
print(set3) #{0, 82, 78, 87, 23, 9, 90, 46}

set1 = {23, 46, 87, 9, 0}
set2 = {82, 78, 90}
set3 = {98, 67, 89}
set4 = set1.union(set2, set3)
print(set4) #{0, 98, 67, 9, 78, 46, 82, 23, 87, 89, 90}
set4 = set1| set2| set3
print(set4) #{0, 98, 67, 9, 78, 46, 82, 23, 87, 89, 90}

set5 = {89, 90, 89, 34 }
tuple1 = (9,0,0,8,9,7,6,5)
dt = set5.union(tuple1)
print(dt) #{0, 34, 5, 6, 7, 8, 9, 89, 90}

# The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.

#The update() method inserts all items from one set into another.
set1 = {65, 87, 54}
set2 = {"a", "b", "c"}
set1.update(set2)
print(set1) #{65, 54, 87, 'b', 'a', 'c'}
#The update() changes the original set, and does not return a new set.

#The intersection() method will return a new set, that only contains the items that are present in both sets.
set1 = {65, 87, 54}
set2 = {45, 35, 54} 
set3 = set1.intersection(set2)
print(set3)#{54}


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & (set2)
print(set3) #{'apple'}
#The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.

#The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1) #{'apple'}


#Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates:
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)#{False, 1, 'apple'}

#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.difference(set2) 
print(set3) #{'cherry', 'banana'}


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3) #{'cherry', 'banana'}
#The - operator only allows you to join sets with sets, and not with other data types like you can with the difference() method.


#Use the difference_update() method to keep only the items from the first set that are not present in the other set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1) #{'banana', 'cherry'}

#The symmetric_difference() method will keep only the elements that are NOT present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3) #{'microsoft', 'google', 'banana', 'cherry'}

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)#{'google', 'cherry', 'banana', 'microsoft'}
# The ^ operator only allows you to join sets with sets, and not with other data types like you can with the symmetric_difference() method.

#The symmetric_difference_update() method to keep the items that are not present in both sets:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)#{'cherry', 'google', 'microsoft', 'banana'}