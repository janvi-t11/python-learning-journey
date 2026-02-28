fruits={"green apple", "lichi", "mango"}
for x in fruits:
    print(x) 
#lichi
#mango
#green apple
print("mango" in fruits)# true 
print("apple"not in fruits) # true
print("apple in fruitss")# false

fruits.add("orange")
print(fruits)#{'mango', 'lichi', 'orange', 'green apple'}

vegetables = {"onion", "brinjal", "potato", "ladyfinger"}
fruits.update(vegetables)
print(fruits)

car= ["bmw", "toyota"]
fruits.update(car)
print(fruits)#{'ladyfinger', 'toyota', 'brinjal', 'orange', 'potato', 'green apple', 'mango', 'lichi', 'onion', 'bmw'}

fruits.remove("onion")
print (fruits) #{'ladyfinger', 'toyota', 'brinjal', 'orange', 'potato', 'green apple', 'mango', 'lichi', 'bmw'}

fruits.pop()
print(fruits) # a random element will get removed {'mango', 'orange', 'ladyfinger', 'green apple', 'potato', 'toyota', 'bmw', 'brinjal'} {lichi}

fruits.discard("ladyfinger")   
print(fruits) #{'toyota', 'brinjal', 'orange', 'potato', 'green apple', 'mango', 'lichi', 'bmw'}

fruits.clear()
print(fruits)#set()

