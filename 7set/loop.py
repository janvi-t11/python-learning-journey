Fruits = {"apple", "banana"}
for x in Fruits:
    print(x)

nums = {1, 2, 3, 2, 4, 1, 5}
for x in nums: 
    if x > 2:
        print(x) 
#output = 3, 4, 5

#some understanding and building strength question
unique_word = set()
while (word := input("enter word:"" ")) != "stop":
    unique_word.add(word)
    print("Unique word count:", len(unique_word))
    

