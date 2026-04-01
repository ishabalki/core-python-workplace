"""
Que 1)Diff between methods and function?
self.
Que 3) Create IPL 2026 players team of your choice.
"""
#Que 2) create 5 classes of your choice and write minimum 2 attributes and 1 method of each class?

#car
class Car:
    def __init__(self,model,colour,speed,brand_name,car_no):
        self.model = model
        self.colour = colour
        self.speed = speed
        self.brand_name = brand_name
        self.car_no = car_no
    def display(self):
        print(self.model,self.colour,self.speed,self.brand_name,self.car_no)
my_car=Car("boleroneo","white",200,"mahirda","MH29CJ3398")
my_car.display()

#icecream
class IceCream:
    def __init__(self, flavor, price, br_name):
        self.flavor = flavor
        self.price = price
        self.brand_name = br_name
    def display(self):
        print(self.flavor, self.price, self.brand_name)
ice = IceCream("Chocolate", 50, "Amul")
ice.display()

#bailgadi
class Bailgadi:
    def __init__(self, owner, wheels, color,has_roof):
        self.owner = owner
        self.wheels = wheels
        self.color = color
        self.has_roof = has_roof
    def display(self):
        print(self.owner, self.wheels, self.color,self.has_roof)
cart = Bailgadi("Ramesh", 2, "Brown",2)
cart.display()

#cooler
class Cooler:
    def __init__(self, brand, price, capacity):
        self.brand = brand
        self.price = price
        self.capacity = capacity
    def display(self):
        print(self.brand, self.price, self.capacity)
cooler1 = Cooler("Symphony", 10000, "10L")
cooler1.display()

#inverter
class Inverter:
    def __init__(self, brand, capacity, has_battery,water_capacity):
    
        self.brand = brand
        self.capacity = capacity
        self.has_battery = has_battery
        self.water_capacity = water_capacity 
    def display(self):
        print("Brand:", self.brand,self.capacity,self.has_battery,self.water_capacity)
inv1 = Inverter("Luminous", "850VA", True,"10L")
inv1.display()

# op=boleroneo white 200 mahirda MH29CJ3398
# Chocolate 50 Amul
# Ramesh 2 Brown 2
# Symphony 10000 10L
# Brand: Luminous 850VA True 10L


#Que 3)Create IPL 2026 players team of your choice.

class player_ipl2026:
    def __init__(self,jn,pn,r,tn,wk):
        self.jersey_no=jn
        self.p_name =pn
        self.runs=r
        self.t_name=tn
        self.wickets=wk
    def display(self):
        print(self.jersey_no,self.p_name,self.t_name,self.runs,self.wickets)

p1 = player_ipl2026(1, "Faf du Plessis", 4000, "RCB", 10)
p2 = player_ipl2026(2, "Virat Kohli", 6000, "RCB", 4)
p3 = player_ipl2026(3, "Glenn Maxwell", 2500, "RCB", 30)
p4 = player_ipl2026(4, "Shahbaz Ahmed", 800, "RCB", 25)
p5 = player_ipl2026(5, "Dinesh Karthik", 3500, "RCB", 5)
p6 = player_ipl2026(6, "Wanindu Hasaranga", 1200, "RCB", 50)
p7 = player_ipl2026(7, "Harshal Patel", 900, "RCB", 60)
p8 = player_ipl2026(8, "Mohammed Siraj", 600, "RCB", 70)
p9 = player_ipl2026(9, "Yuzvendra Chahal", 500, "RCB", 95)
p10 = player_ipl2026(10, "David Willey", 400, "RCB", 40)
p11 = player_ipl2026(11, "Rajat Patidar", 1100, "RCB", 2)
p12 = player_ipl2026(12, "Shivam Dube", 1300, "RCB", 15)
p13 = player_ipl2026(13, "Anuj Rawat", 300, "RCB", 0)
p14 = player_ipl2026(14, "Mahipal Lomror", 200, "RCB", 5)
p15 = player_ipl2026(15, "Suyash Prabhudessai", 100, "RCB", 0)
p16 = player_ipl2026(16, "Kyle Jamieson", 400, "RCB", 20)
p17 = player_ipl2026(17, "Josh Hazlewood", 50, "RCB", 30)
p18 = player_ipl2026(18, "Faf du Plessis Jr.", 150, "RCB", 5)
p19 = player_ipl2026(19, "Rajat Patidar Jr.", 200, "RCB", 1)
p20 = player_ipl2026(20, "Prithvi Raj", 100, "RCB", 0)
p21 = player_ipl2026(21, "AB de Villiers", 5000, "RCB", 10)
p22 = player_ipl2026(22, "Devdutt Padikkal", 2500, "RCB", 2)
p23 = player_ipl2026(23, "Josh Philippe", 800, "RCB", 0)
p24 = player_ipl2026(24, "Shreyas Gopal", 300, "RCB", 20)
p25 = player_ipl2026(25, "Glenn Maxwell Jr.", 600, "RCB", 15)

RCB_Team =[]
RCB_Team = []
RCB_Team.append(p1)
RCB_Team.append(p2)
RCB_Team.append(p3)
RCB_Team.append(p4)
RCB_Team.append(p5)
RCB_Team.append(p6)
RCB_Team.append(p7)
RCB_Team.append(p8)
RCB_Team.append(p9)
RCB_Team.append(p10)
RCB_Team.append(p11)
RCB_Team.append(p12)
RCB_Team.append(p13)
RCB_Team.append(p14)
RCB_Team.append(p15)
RCB_Team.append(p16)
RCB_Team.append(p17)
RCB_Team.append(p18)
RCB_Team.append(p19)
RCB_Team.append(p20)
RCB_Team.append(p21)
RCB_Team.append(p22)
RCB_Team.append(p23)
RCB_Team.append(p24)
RCB_Team.append(p25)

for player_ipl2026 in RCB_Team:
    player_ipl2026.display()