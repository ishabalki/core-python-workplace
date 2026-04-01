"""
arguments=it means a value or data in function while use a function calling time.
parameters= parameters means variable names that we write at the time function defination.

types of arguments=there arevfew types of arguments in a function
1)positional arguments:-> position of arguments are importaant.
2)keywords arguments:-> in this arguments position are not important 
 we pass the data in key and value.
3)default arguments:-> You give a default value to parameters
If user doesn't pass value default is used
4)arbitary arguments its also known a 4)variable length arguments:-> Used when you donot know how many arguments will be passed.
   a)positional arbitary:->Accepts multiple values as a tuple
   b)keyword arbitary:->Accepts multiple key-value pairs as a dictionary
"""

def add(a,b): #a and b are parameters
    return a + b
print(add(10,30))  #10,30 is a variable 

#position 
def add(n1,n2):
    return n1+n2
a=10
b=20
print(add(a,b))

def subtwo(n1,n2):
    return n1-n2
a=10 #in this way the position is important
b=20
print(subtwo(a,b))
print(subtwo(b,a)) #change its position and position is important

#keyword arguments
def subtwo(n1,n2):
    return n1-n2
a=10
b=20
r1=subtwo(n1=b ,n2=a)
r2=subtwo(30,67)
print(r1)
print(r2)

#default 
def greet(name="Guest"):
    return "Hello " + name

print(greet("Ravi"))   # Hello Ravi
print(greet())         # Hello Guest

#arbitary
#positional
def add_all(*nums):
    return sum(nums)

print(add_all(1, 2, 3))       # 6
print(add_all(10, 20, 30, 40)) # 100

#keyword
def details(**data):
    return data

print(details(name="Ravi", age=20))