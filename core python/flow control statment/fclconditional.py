"""
flow control statment
1)conditionl
if,if-else,if-elif-else
    2)iterative
for ,while Loop
    3)transfer

1)if-else
if condition:
    body of if
else:
body of else:
else check only one codition.


if-elif-else=to check multiple condition.
    sry->
    if condition1:
        if body
    elif condition2:
        elif body
    elif n no of condition:
        elif body
    else:
        else body
"""


#write a program print given no even or odd?
# num=-12
# if num % 2==0:
#     print("num is even")
# else:
#     print("num is odd")
# op=num is even

# num=13
# if num % 2==0:
#     print("num is even")
# else:
#     print("num is odd")
# op=num is odd

#you have given a number.
#if the number is divisible by 3 disply "fizz"
#if the number is divisible by 5 display "buzz"
#if the number is divisible 3 & 5 both display "fizzbuzz"

# num=15
# if num % 3==0 and  num % 5==0:
#     print("fizzbuzz")
# elif num % 5==0:
#     print("buzz")
# elif num % 3==0:
#     print("fizz")
# else:
#     print("not divisible by 3 & 5")
    # op=fizzbuzz

# num=53
# if num % 3==0 and  num % 5==0:
#     print("fizzbuzz")
# elif num % 5==0:
#     print("buzz")
# elif num % 3==0:
#     print("fizz")
# else:
#     print("not divisible by 3 & 5")
# op=not divisible by 3 & 5

#you have one list of students marks.
# create two sub lists for even and odd marks students.

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
stud.append(76)
stud.append(63)
stud.append(71)
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
