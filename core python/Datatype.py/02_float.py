price= 100
runs= 40
wickets = 3
temp = -20

# print("The price is",price)
# print(type(price)) #<class 'int'> indicate that price is an integer
# print("The runs is",runs)
# print(type(runs))
# print("The wickets is",wickets)
# print(type(wickets))
# print("The temprature is",temp)
# print(type(temp)) 

petrol_price = 103.45
print("The petrol price",price)
print(type(petrol_price))    #<'class float'> indicate the petrol price


actual_op= price + petrol_price
expected_op = 203.45

if actual_op == expected_op:
   print("The test case passed")