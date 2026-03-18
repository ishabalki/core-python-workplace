#task1
"""
  This program defines a function to check whether a given number is prime or not.
"""
num = 9

def prime_number(num):
    count = 0  
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

prime_number(num)

"""
op=
9 is not a prime number
"""



#task2 the program print 1 to 7 no using while loop

# program 1
var = 1
def numbers(var):
    while(var <= 7):
        print(var)
        var += 1
numbers(var) 
"""
op=
1
2
3
4
5
6
7
"""

# program2 create a table of any number uisng while loop
def table(num): 
    i = 1
    while i <= 10:
        res = num * i
        print(f"{num} * {i} = {res}")
        i += 1
num = int(input("Enter a number to print its table: "))
table(num)

"""
op=Enter a number to print its table: 5
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50
"""
#task3 palindrome 
def palindrome(text):
    r_text = ""
    for ch in text:
        r_text = ch + r_text 
    print("Reversed string:", r_text)
    if text == r_text:
        print(f"{text} is a palindrome")
    else:
        print(f"{text} is not a palindrome")

palindrome("ritik")

"""
op=Reversed string: kitir
ritik is not a palindrome
"""
