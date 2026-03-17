stud=[]
stud.append(42)
stud.append(43)
stud.append(53)
stud.append(73)
stud.append(22)
stud.append(32)
stud.append(2)
stud.append(90)
stud.append(67)
stud.append(4)
stud.append(78)
print(stud)

even_marks=[]
odd_marks=[]

for i in stud:
    if i % 2 == 0:
        even_marks.append(i)
    else:
        odd_marks.append(i)

print("even_marks:", even_marks)
print("odd_marks:", odd_marks)

