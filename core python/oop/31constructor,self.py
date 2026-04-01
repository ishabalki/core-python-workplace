"""
what is constructor?
:->In Object-Oriented Programming (OOP), a constructor is a special method used to initialize an object when it is created.
-it is a special type of method.
-the name of constructor is__init__
-constructor get automatically invoked(called)at the time of object creation.
-the job of constructor is to initiallize attributes into memory
-it inialllize object into memory
-there is no written statment in a constructor
-__methodName__  methods are called dunder(dubleunderscore) methods in python
:->there are two types of constructor
     1)default
     2)paramitrized
:-> 

"""

#task1:-> in ipl 2026 ,players has jersey no, p_name,runs,t_name and wickets,there is one operation with player which display players name and team name. 
class player:
    def __init__(self,jn,pn,r,tn,wk):
        self.jersey_no=jn
        self.p_name =pn
        self.runs=r
        self.t_name=tn
        self.wickets=wk
    def display(self):
        print(self.jersey_no,self.p_name,self.t_name,self.runs,self.wickets)

p1=player(18,"virat kolhi",6767,"RCB",1)
p2 =player(7, "MS Dhoni", 4876, "CSK", 0)
p3 =player(10, "Rashid Khan", 120, "GT", 9)
p4 =player(99, "Hardik Pandya", 2150, "MI", 8)
p5 =player(9, "Shubman Gill", 3100, "KKR", 5)

p1.display() # it a a method or a function we use for a display the data.
p2.display()
p3.display()
p4.display()
p5.display()

