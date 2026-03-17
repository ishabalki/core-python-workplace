#  relational comparison operatore-->
# >,<,>=,<=,
# equality 
# 1)==, 2)!=
#to check the no it negative or positive
# to type a coditition

#logical operator
# 1)and= if all the operands are true then and then only output is true if any one operatore is false output is false
# 2)or=if all the operands are false then and only op is false and one oerand is true gives the op is true.
# 3)not=inversion/complement

#and
# a=True
# b=False
# c=True
# print(a and b and c)
# op=False

# d=True
# e=True
# print(d and e)
# op= True

#assignment operator-->
#a=10
#l=[1,2,3,4]

#composite assignment--> reuse the same variable,and arithmaatic and assign operator use create a composite assignment operator.
# a=10
# a=a+5
# a+=5
# print(a)


#bitwise operator
# ^=xor=when both value are same op is 0 and diff value op is 1.

# | A | B | XOR | **XNOR** |
# | - | - | --- | -------- |
# | 0 | 0 | 0   | **1**    |
# | 0 | 1 | 1   | **0**    |
# | 1 | 0 | 1   | **0**    |
# | 1 | 1 | 0   | **1**    |


# print(3|5)

# print(3 & 5)

# print(3^5)

# print(3>>5)

# print(~(3^5)) #use for ~ gives the ^ this operation

# print(3<<2)

#special operator
# 1)is=identity op 
# 2)=membership op

a=123
b=123
# print(a is b)


# print(10 in [1,5,6,7,10])
print(id(a)==id(b))
print("z" in "instgram")
