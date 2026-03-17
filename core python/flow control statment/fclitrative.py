"""
iterative
1)for=entry control loop.DRY,we know 
2)while=
"""

# write a program 1 to 5 on console using for loop

# for i in range(1,6):
#         print(i)

# for i in (1,2,3,4,5):
#         print(i)

# for i in [1,2,3,4,5]:
#         print(i)

# for i in {1,2,3,4,5}:
#         print(i)

#print 100 to 5 on console
# for i in range(100,4,-1):
#     print(i)

#write a program to print all odd no from 23 to 67.
# for i in range(23,67,2):
#     print(i)

#step 2
# for i in range(23,67):
#     if i % 2!=0:
#         print(i)

# to perform even no
# for i in range(23,67):
#     if i % 2!=1:
#         print(i)

#wap to check the given no is prime or not?
#the prime no is no is divisible by 1 and itself

# #way1
num = 7
count=0 # it use for a count a no means 2 no is divisible by prime no

for i in range(1,num+1):
    if num % i == 0:
        count += 1 
if count == 2: #2 no is only divisible by prime no
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")

# #wya2
num = 11
count=0 

for i in range(2,num//2 + 1):
    if num % i == 0:
        count += 1 
if count >= 0: 
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")
# way3
num = 7
count=0 

for i in range(1,num//2):
    if num % i == 0:
        count += 1 
if count == 1: 
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")

# #way4
num = 9
count=2 

for i in range(2,num):
    if num % i == 0:
        count += 1 
if count == 0: 
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")

# #way5 using the break
num = 5
count=0

for i in range(2,num//2):
    if num % i == 0:
        count += 1 
        break
if count == 0: 
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")











 


       
