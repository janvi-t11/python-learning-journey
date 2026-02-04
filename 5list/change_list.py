li1 = ["apple", "peach" , "curd", "bread"]
print(li1) #['apple', 'peach', 'curd', 'bread']
li1[1]= "cherry"
print(li1) #['apple', 'cherry', 'curd', 'bread']
li1[2:4] = ["banana", "orange"]
print(li1) #['apple', 'cherry', 'banana', 'orange']

thislist = ["apple", "banana", "cherry"]

thislist[1:3] = ["watermelon"]

print(thislist)

thislist.insert(1, "pineapple")
print(thislist)

