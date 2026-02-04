#and operator
a = 15 #1111
b = 14 #1110
print(a & b) #1110 (Answer:14) Sets each bit to 1 if both bits are 1

#or operator
a = 10 #1010
b = 6  #0110
print(a | b) #1110 (Answer:14) Sets each bit to 1 if at least one of the two bits is 1

#xor operator
a = 6 #0110
b = 9 #1001
print(a ^ b) #1111 (Answer:15) Sets each bit to 1 if only one of the two bits is 1

#not operator
a = 5 #0101
print(~a) #-6 (Answer:-6) Inverts all the bits

#left shift operator
a = 3 #0011
print(a<<2) #1100 (Answer:12) Shifts the bits to the left and fills 0 on voids

#right shift operator
a = 16 #10000
print(a>>2) #00100 (Answer:4) Shifts the bits to the right and fills 0 on voids