# create dist
movies25_db={}
# #movie casting detail
cast_dhur=["ranveer singh","akashay khanna","sanajay dutt","sara arjun"]
cast_war2=["Hrithik roshan","NTR Jr","kiara advani","annaya pandey"]
cast_singhamAgain=movies_db = ["Ajay Devgn", "Akshay Kumar", "Deepika Padukone", "Tiger Shroff"]
cast_chhava=["vicky kaushal","rshmika mandana","akashay khanna"]
cast_animal=["Ranbir Kapoor", "Anil Kapoor", "Bobby Deol", "Tripti Dimri"]

#add to dictionary
movies25_db["Dhurandhar"] = cast_dhur
movies25_db["War 2"] = cast_war2
movies25_db["Singham Again"] = cast_singhamAgain
movies25_db["chhava"] = cast_chhava
movies25_db["Animal"] = cast_animal
# print(movies25_db)

#using a loop way 1 for count key 
# for k in movies25_db:
#     print(movies25_db.get(k))

# #using for count k,v

# count=0
# for k,v in movies25_db.items():
#     for name in v:
#         if name== "akashay khanna":
        
#             count=count+1
#             print(k)
# print(count)



# count=0
# for k,v in movies25_db.item():
#     for name in v:
#         if name in v:
#             if name=="ranveer singh":
#                 count=count+1
#                 print(k)
# print(count)

#print the name from the movie
# print(movies25_db["Dhurandhar"][0])
# i = movies25_db.get("Dhurandhar")
# print(i[0])
# print(movies25_db.get("Dhurandhar")[0])

#its print a first no
print(movies25_db["Dhurandhar"][1])

#its revers the name
# print(movies25_db["Dhurandhar"][1][::-1])

# #its print the one letter
# print(movies25_db["Dhurandhar"][1][6])
#o/p y

# display names of all actor and actress 
# for k,v in movies25_db.items():
#     print(k,"--->")
#     for name in v:
#         print(name)

# Dhurandhar --->
# ranveer singh
# akashay khanna
# sanajay dutt
# sara arjun

# War 2 --->
# Hrithik roshan
# NTR Jr
# kiara advani
# annaya pandey

# Singham Again --->
# Ajay Devgn
# Akshay Kumar
# Deepika Padukone
# Tiger Shroff

# chhava --->
# vicky kaushal
# rshmika mandana
# akashay khanna

# Animal --->
# Ranbir Kapoor
# Anil Kapoor
# Bobby Deol
# Tripti Dimri

# for k,v in movies25_db.items():
#     print(k ,"--->")
    
#     for name in v:
#       print(name)
#       for nm in name.split():
#         print("\t\t",nm)

# Dhurandhar --->
# ranveer singh
#                  ranveer
#                  singh
# akashay khanna
#                  akashay
#                  khanna
# sanajay dutt
#                  sanajay
#                  dutt
# sara arjun
#                  sara
#                  arjun
# War 2 --->
# Hrithik roshan
#                  Hrithik
#                  roshan
# NTR Jr
#                  NTR
#                  Jr
# kiara advani
#                  kiara
#                  advani
# annaya pandey
#                  annaya
#                  pandey
# Singham Again --->
# Ajay Devgn
#                  Ajay
#                  Devgn
# Akshay Kumar
#                  Akshay
#                  Kumar
# Deepika Padukone
#                  Deepika
#                  Padukone
# Tiger Shroff
#                  Tiger
#                  Shroff
# chhava --->
# vicky kaushal
#                  vicky
#                  kaushal
# rshmika mandana
#                  rshmika
#                  mandana
# akashay khanna
#                  akashay
#                  khanna
# Animal --->
# Ranbir Kapoor
#                  Ranbir
#                  Kapoor
# Anil Kapoor
#                  Anil
#                  Kapoor
# Bobby Deol
#                  Bobby
#                  Deol
# Tripti Dimri
#                  Tripti
#                  Dimri

#for print the one by one character
for k,v in movies25_db.items():
    print(k ,"--->")
    
    for name in v:
      print(name)
      for nm in name.split():
        print("\t\t",nm)
        for ch in nm:
            print("\t\t\t",ch)
            
# Dhurandhar --->
# ranveer singh
#                  ranveer
#                          r
#                          a
#                          n
#                          v
#                          e
#                          e
#                          r
#                  singh
#                          s
#                          i
#                          n
#                          g
#                          h
# akashay khanna
#                  akashay
#                          a
#                          k
#                          a
#                          s
#                          h
#                          a
#                          y
#                  khanna
#                          k
#                          h
#                          a
#                          n
#                          n
#                          a
# sanajay dutt
#                  sanajay
#                          s
#                          a
#                          n
#                          a
#                          j
#                          a
#                          y
#                  dutt
#                          d
#                          u
#                          t
#                          t
# sara arjun
#                  sara
#                          s
#                          a
#                          r
#                          a
#                  arjun
#                          a
#                          r
#                          j
#                          u
#                          n
# War 2 --->
# Hrithik roshan
#                  Hrithik
#                          H
#                          r
#                          i
#                          t
#                          h
#                          i
#                          k
#                  roshan
#                          r
#                          o
#                          s
#                          h
#                          a
#                          n
# NTR Jr
#                  NTR
#                          N
#                          T
#                          R
#                  Jr
#                          J
#                          r
# kiara advani
#                  kiara
#                          k
#                          i
#                          a
#                          r
#                          a
#                  advani
#                          a
#                          d
#                          v
#                          a
#                          n
#                          i
# annaya pandey
#                  annaya
#                          a
#                          n
#                          n
#                          a
#                          y
#                          a
#                  pandey
#                          p
#                          a
#                          n
#                          d
#                          e
#                          y
# Singham Again --->
# Ajay Devgn
#                  Ajay
#                          A
#                          j
#                          a
#                          y
#                  Devgn
#                          D
#                          e
#                          v
#                          g
#                          n
# Akshay Kumar
#                  Akshay
#                          A
#                          k
#                          s
#                          h
#                          a
#                          y
#                  Kumar
#                          K
#                          u
#                          m
#                          a
#                          r
# Deepika Padukone
#                  Deepika
#                          D
#                          e
#                          e
#                          p
#                          i
#                          k
#                          a
#                  Padukone
#                          P
#                          a
#                          d
#                          u
#                          k
#                          o
#                          n
#                          e
# Tiger Shroff
#                  Tiger
#                          T
#                          i
#                          g
#                          e
#                          r
#                  Shroff
#                          S
#                          h
#                          r
#                          o
#                          f
#                          f
# chhava --->
# vicky kaushal
#                  vicky
#                          v
#                          i
#                          c
#                          k
#                          y
#                  kaushal
#                          k
#                          a
#                          u
#                          s
#                          h
#                          a
#                          l
# rshmika mandana
#                  rshmika
#                          r
#                          s
#                          h
#                          m
#                          i
#                          k
#                          a
#                  mandana
#                          m
#                          a
#                          n
#                          d
#                          a
#                          n
#                          a
# akashay khanna
#                  akashay
#                          a
#                          k
#                          a
#                          s
#                          h
#                          a
#                          y
#                  khanna
#                          k
#                          h
#                          a
#                          n
#                          n
#                          a
# Animal --->
# Ranbir Kapoor
#                  Ranbir
#                          R
#                          a
#                          n
#                          b
#                          i
#                          r
#                  Kapoor
#                          K
#                          a
#                          p
#                          o
#                          o
#                          r
# Anil Kapoor
#                  Anil
#                          A
#                          n
#                          i
#                          l
#                  Kapoor
#                          K
#                          a
#                          p
#                          o
#                          o
#                          r
# Bobby Deol
#                  Bobby
#                          B
#                          o
#                          b
#                          b
#                          y
#                  Deol
#                          D
#                          e
#                          o
#                          l
# Tripti Dimri
#                  Tripti
#                          T
#                          r
#                          i
#                          p
#                          t
#                          i
#                  Dimri
#                          D
#                          i
#                          m
#                          r
#                          i











            






