# level=2
div_A= { 1:{"name":"jay","sub":["maths","phy","chem"],"marks":[89,71,99]},
         2:{"name":"pavan","sub":["maths","phy","chem"],"marks":[66,55,77]},
         3:{"name":"kiran","sub":["maths","phy","chem"],"marks":[88,99,99]}
       }
for rollno,student in div_A.items():
    m=student.get("marks")
    avg=sum(m)/len(m)
    print(rollno,"-->",student.get("name","-->",avg"))

 