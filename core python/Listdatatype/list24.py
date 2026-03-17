# list is the collective data type
# ---collective datatype
# ----heterogenious collection
# ----enclosed by [] seprated by (,)
# -----order 
# -----mutable
# -----allow duplicates
# ----we can fetch data using indexing and slicing
# ---it is a sequence data type

# l1 = []
# # print(type(l1))

# l2 = [10,20,30]
# print(l2)
# print(type(l2))

# l3 = [10,20,30,10]
# print(l3)

# l4 = [10,10.5,"ritik",10+20j,True,[10,20,30],(1,2,3),{3,9,6},{1:1,2:4}]
# print(l4)

# l5 = ["10","20","30","isha"]
# l5.extend([1000])
# print(l5)
# print(15[-1])

# l4 = [20,30,40]
# l4.append(1000)
# print(l4)

l3 = [20,10,40]
l3.insert(-2,30)
print(l3)

# l1 =[10,20,30,40]
# print(dir(l1))

# # l1.clear()
# l2 =l1.copy()
# print("l1:",12)
# print("l2:",l1)

# l3=l1
# print("l3:",l3)

# l2 =[]
# print(l2.count(10))

# print(l1.index(30))

# # print(l1.pop()) #kabhibhi last vali value pop krega #40
# print(l1)

# # print(l1.pop(2)) #pop 30 as a data dono trf se same fetch kr skte hai
# # print(l1.pop(-2))  #30
# # l1.remove(100) #its give a value error

# print(l1.reverse()) #its change my string
# print(l1)
# # print("after:",l1)
# # print(reversed(l1)) #<list_reverseiterator object at 0x0000027CEF565C30>

# print(sorted(l1))

# l6 =[9,40,8,4,5,2,6,7]
# # 
# print(l6.sort())

# str1 = "ISHA"
# print(sorted(str1))

# print(reversed(str1)) #<reversed object at 0x000001B5763D5F30>
# print(set(reversed(str1)))
# l3 = []
# even_list = 0
# even = 0

#    for i in range l2:
#       if i % 2 == 0:
#          l3.append (i)
#          print(l6)
#          even = even + 1
# print(l3)
# print(even)
# print(even_list)