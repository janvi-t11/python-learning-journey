#Unpacking tuple item (In Python, we are also allowed to extract the values back into variables. This is called "unpacking":)
cars = ("BMW", "MERCEDES", "TOYOTA")
(circle, triangle, rectangle) = cars
print(circle) #BMW
print(triangle) #MERCEDES
print(rectangle) #TOYOTA 

phones = ("samsung", "oppo", "infinix", "vivo", "iphone") 
(black, blue, white, *red) = phones
print(black) #samsung
print(blue) #oppo
print(white) #infinix
print(red) #['vivo', 'iphone']

subjects = ("maths", "science", "english", "social", "history", "geography")
(numbers, experiments, *arts, ancient, topology) = subjects
print(numbers) #maths 
print(experiments) #science
print(arts) #['english', 'social']
print(ancient) #history
print(topology) #geography
