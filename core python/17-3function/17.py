# def addtwo(num1, num2):
#     res = num1 + num2
#     print(f"Addition of {num1} and {num2} =", res)
# addtwo(5,10)

# """
# add two numbers of this code
# """
# #gmail has login check operation which accept user name and password from user and display on screen.
# def gmail_login(username,password):
#     print("username:",username)
#     print("password:",password)

#     if username =="ABC" and password=="1234":
#         print("login sucessfull!")
#     else:
#         print("login_failed")   
# gmail_login("ABC","1234")


# #cube of any number
# def cube():
#     num = int(input("Enter a number: "))
#     print("Cube =", num * num * num )

# cube()

# #print given list square
# lst = [2, 4, 5, 6, 7]

# def square_lst(lst):
#     for i in lst:
#         print(i * i)

# square_lst(lst)

# #to define a reverse no
# def rev(num):
#     print(str(num)[::-1])

# n = int(input("Enter number: "))
# rev(n)

#Write a function that takes two numbers and prints their subtraction
# def addtwo(num1,num2):
#     res = num1 - num2
#     print(F"subtraction of {num1} and {num2}=",res)
# addtwo(10,4)
# op=subtraction of 10 and 4= 6

#Create a function that takes a number and prints whether it is even or odd

# def even_odd(num):
#     if num % 2 == 0:
#         print("the num is even=",num)
#     else:
#         print("the num is odd=",num)

# even_odd(5)
# even_odd(10)
# op=the num is odd= 5
# the num is even= 10


#Take a number from user and print its square using a function.
# def square():
#     num=int(input("enter a number:",))
#     print("square=",num * num )
# square()
# op=enter a number:23
# square= 529

#Write a function that takes two numbers and prints the larger one
def two_num(num1, num2):
    if num1 > num2:
        print("num1 is the largest number")
    elif num2 > num1:
        print("num2 is the largest number")
    else:
        print("Both numbers are equal")
two_num(12,34)
# op=num2 is a largest number