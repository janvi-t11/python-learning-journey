#slicing
a = "Hello, john"
print(a[3:8]) #lo, j
print(a[0:6]) #Hello,
print(a[:5]) #Hello
print(a[2:]) #llo, john
print(a[:]) #Hello, john
print(a[-9:-3]) #lo, j

#slice with skipping
b = "abcdefghijklmnopqrstuvwxyz"
print(b[1:8:3]) #beh
print(b[0:9:5]) #af
print(b[5:20:5]) #fjou
print(b[::4]) #aeimquy