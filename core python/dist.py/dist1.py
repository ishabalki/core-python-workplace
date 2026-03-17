
# my_dist={}
# print(type(my_dist))

# db = {}
# db[1]="jay"
# db[1]="vijay"
# print(db[1])
# db[2]="vijay"
# print(db[2])


# stud_db={}
# stud_db[1]="jay"
# stud_db[2]="viru"
# stud_db[3]="basanti"
# stud_db[4]="rakhi"
# print(stud_db[1])
# print(stud_db[2])
# print(stud_db[3])
# print(stud_db[4])

# v1=stud_db[30] #key error
# print(v1)

# stud_db={}
# print(type(stud_db))
# print(stud_db)

# stud_db[1]="isha"
# stud_db[20]=30
# stud_db[2]="laxmi"
# print(stud_db)

# stud_db={}
# for k in stud_db:
#     print(k,"-->",stud_db.get(k),stud_db[k])

# for k in stud_db:
#     print(stud_db[k],dict.get(key))
stud_db={}
stud_db[1]="jay"
stud_db[2]="viru"
stud_db[3]="basanti"
stud_db[4]="rakhi"
print(stud_db[1])
print(stud_db[2])
print(stud_db[3])
print(stud_db[4])

# for t in stud_db.item():
#     print(t)
for t in stud_db.item():
    k,v=t
    print(k ,"-->", v)