#print numbers from 1 to 100
i = 1
while i <= 100:
    print(i)
    i+=1


#print number from 100 to 1
i = 100
while i >=1:
    print(i)
    i-=1

#print the multiplication table of n number
#my logic
i = 5
while i <=50:
    print(i)
    i+=5 #it would print 5 table till 5*10=50

    
#staandard logic
i = 1
while i<=10:
    print(6*i)
    i+=1 #it would print the table you just need to change number inside the print

#print the list in loop
square = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(square):
    print(square)
    idx += 1

#search for a number x in this tuple using loop
square = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x= 16
i = 0
while i < len(square):
    if square[i]== x:
        print("found at idx", i)
        break
    i += 1
 
# Question 1: ATM Withdrawal System
# A user has ₹10,000 in their bank account.
# Keep asking the user to enter withdrawal amount:
# If amount ≤ balance → deduct and show remaining balance
# If amount > balance → show “Insufficient Balance”
# Stop when user enters 0
# At the end, print final balance

atm = 10000

while True:
    user = int(input("Enter amount to withdraw (0 to stop): "))

    if user == 0:
        print("Transaction ended")
        break

    if user > atm:
        print("Insufficient balance")
    else:
        atm -= user
        print("Amount withdrawn successfully")
        print("Remaining balance:", atm)

print("Final balance:", atm)

# Question 2: Password Retry System
# User has 3 attempts to enter correct password.
# Correct password = "janvi123"
# Keep asking until correct password entered
# If wrong, reduce attempts
# If attempts become 0 → print “Account Locked”
# If correct → print “Login Successful”

password = "janvi123"
attempt = 3
while attempt > 0:
    user=input ("enter password:" + "")
    if user == password:
        print("login successful")
        break
    else:
        attempt -= 1
        print("Wrong password. Attempts left:", attempt)
        if attempt == 0:
            print("account locked")

 

