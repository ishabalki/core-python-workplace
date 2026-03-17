#WAP TO check the given no is prime or not

#way 1
num = 7
count=0 # it use for a count a no means 2 no is divisible by prime no

for i in range(1,num+1):
    if num % i == 0:
        count += 1 
if count == 2: #2 no is only divisible by prime no
    print(num,"is a prime number")
#   op=7 is a prime number


#way 2
num = 7
count=0

for i in range(1,num//2+1):
    if num % i == 0:
        count += 1 
if count == 1: #2 no is only divisible by prime no
    print(num,"is a prime number")
else:
    print(num,"is a not prime number")

# op=7 is a prime number

#way3
num = 7
count=2

for i in range(2,num//2+1):
    if num % i == 0:
        count += 1 
if count == 2: 
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")

#   op=7 is a prime number

#way=4
num = 7
count=0

for i in range(2,num//2):
    if num % i == 0:
        count += 1 
if count == 0: 
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")

#WAY5
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
#   op=5 is a prime number