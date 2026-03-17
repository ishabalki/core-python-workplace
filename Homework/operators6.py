#integer+integer
A=6
B=10
result = A+B
print("result:",result)
# op=result: 16

#int-int
A=6
B=10
result = A-B
print("result:",result)
# op=result: -4

#int*int
A=6
B=10
result = A*B
print("result:",result)
# op=result: 60

#int/int
A=6
B=10
result = A/B
print("result:",result)
#op=result:0.6

#int//int
A=6
B=10
result = A//B
print("result:",result)
# op=result:0


#int%int
A=6
B=10
result = A%B
print("result:",result)
# op=result:6

#int+float
A=6
B=10.5
result = A+B
print("result:",result)
# op=result:16.5

#int-float
A=6
B=10.5
result = A-B
print("result:",result)
# result: -4.5

#int*float
A=6
B=10.5
result = A*B
print("result:",result)
# result: 63.0

# int/float
A=6
B=10.5
result = A/B
print("result:",result)
# result: 0.5714285714285714

# int//float
A=6
B=10.5
result = A//B
print("result:",result)
# result: 0.0

# int%float
A=6
B=10.5
result = A%B
print("result:",result)
# result: 6.0

#int+string
num=5
s=("isha")
result=num + s
print(result) #its not add directly to use the method add and combine 
#means string ko int kre ya int ko string,gives the type error

#int-string
num=5
s=("isha")
result=num - s
print(result)
#type error

#int*string
num=5
s=("isha")
result=num*s
print(result)
#type error

#int//string
num=5
s=("isha")
result=num//s
print(result)
#type error

#int/string
num=5
s=("isha")
result=num/s
print(result)
#type error


#int%string
num=5
s=("isha")
result=num%s
print(result)
#type error

#string+string
p=("nutan")
s=("isha")
result=p + s
print(result)
# result:nutanisha 

#string-string
p=("nutan")
s=("isha")
result=p-s
print(result)
#type error

#string*string
p=("nutan")
s=("isha")
result=p*s
print(result)
#type error

#string//string
p=("nutan")
s=("isha")
result=p//s
print(result)
#type error

#string/string
p=("nutam")
s=("isha")
result=p/s
print(result)
#type error


#string%string
p=("nutan")
s=("isha")
result=p%s
print(result)
#type error

#int+list
int=10
list=["2,3,4,5,6"]
result=int+list
print(result)
# type error 

#int-list
int=10
list=["2,3,4,5,6"]
result=int-list
print(result)
# type error 

#int*list
int=10
list=["2,3,4,5,6"]
result=int*list
print(result)
# type error 

#int/list
int=10
list=["2,3,4,5,6"]
result=int/list
print(result)
# type error

#int//list
int=10
list=["2,3,4,5,6"]
result=int//list
print(result)
# type error

#int%list
int=10
list=["2,3,4,5,6"]
result=int%list
print(result)
# type error 

#string+int
p=("nutan")
s=10
result=p+s
print(result)
# op=type error 

#strint-int
p=("nutan")
s=10
result=p-s
print(result)
# op=type error

#string*int
p=("nutan")
s=10
result=p*s
print(result)
# op=utannutannutannutannutannutannutannutannutannutan

#strinh/int
p=("nutan")
s=10
result=p/s
print(result)
# op=type error

#string//int
p=("nutan")
s=10
result=p//s
print(result)
# op=type error

#string%int
p=("nutan")
s=10
result=p%s
print(result)
# op=type error

#list+list
l1=[2,3,4,5,6]
l2=[7,8,9,10]
result=l1+l2
print(result)
# op=result:[2, 3, 4, 5, 6, 7, 8, 9, 10]

#list-list
l1=[2,3,4,5,6]
l2=[7,8,9,10]
result=l1-l2
print(result)
# op=typeerror

#list*list
l1=[2,3,4,5,6]
l2=[7,8,9,10]
result=l1*l2
print(result)
# op=typeerror

#list/list
l1=[2,3,4,5,6]
l2=[7,8,9,10]
result=l1/l2
print(result)
# op=typeerror

# list//list
l1=[2,3,4,5,6]
l2=[7,8,9,10]
result=l1//l2
print(result)
# op=typeerror

# list%list
l1=[2,3,4,5,6]
l2=[7,8,9,10]
result=l1%l2
print(result)
# op=typeerror

# list+int
l1=[2,3,4,5,6]
int=10
result=l1+int
print(result)
# op=typeerror

# list-int
l1=[2,3,4,5,6]
int=10
result=l1-int
print(result)
# op=typeerror

# list*int
l1=[2,3,4,5,6]
int=10
result=l1*int
print(result)
# op=[2, 3, 4, 5, 6, 2, 3, 4, 5, 6, 2, 3, 4, 5, 6, 2, 3, 4, 5, 6, 2, 3, 4, 5, 6, 2, 3, 4, 5, 6, 2, 3, 
# 4, 5, 6, 2, 3, 4, 5, 6, 2, 3, 4, 5, 6, 2, 3, 4, 5, 6]

# list/int
l1=[2,3,4,5,6]
int=10
result=l1/int
print(result)
# op=typeerror

# list//int
l1=[2,3,4,5,6]
int=10
result=l1//int
print(result)
# op=typeerror

# list%int
l1=[2,3,4,5,6]
int=10
result=l1%int
print(result)
# op=typeerror

# #tuple+tuple
t1=(20,)
t2=(10,)
result=t1+t2
print(result)
# op=(20, 10)

# tuple-tuple
t1=(20,)
t2=(10,)
result=t1-t2
print(result)
# op=typeerror

# tuple/tuple
t1=(20,)
t2=(10,)
result=t1/t2
print(result)
# op=typeerror

# tuple*tuple
t1=(20,)
t2=(10,)
result=t1*t2
print(result)
# op=typeerror

# tuple//tuple
t1=(20,)
t2=(10,)
result=t1//t2
print(result)
# op=typeerror

# tuple%tuple
t1=(20,)
t2=(10,)
result=t1%t2
print(result)
# op=typeerror

#tuple+int
t1=(10,)
int=10
result=t1+int
print(result)
# op=typeerror

#tuple+int
t1=(10,)
int=10
result=t1+int
print(result)
# op=typeerror

#tuple-int
t1=(10,)
int=10
result=t1-int
print(result)
# op=typeerror

#tuple*int
t1=(10,)
int=10
result=t1*int
print(result)
# op=typeerror

#tuple/int
t1=(10,)
int=10
result=t1/int
print(result)
# op=typeerror

#tuple//int
t1=(10,)
int=10
result=t1//int
print(result)
# op=typeerror

#tuple%int
t1=(10,)
int=10
result=t1%int
print(result)
# op=typeerror