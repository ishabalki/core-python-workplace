str2 ="ritik"
r_str2 = " "
for ch in str2:
    r_str = ch + r_str
print(r_str)
if str2 == r_str2:
     print("palindrome")
 else:
     print("not palindrome")

# num1 = 121
# c_str1 = str(num1)
# c_str = "  "

# for i in c_str1:
#     r_str = 1 + r_str


# r_num = int(r_str)
# print(r_num)
# print(type(r_num))

# if num1 == r_num:
#     print("digit palindrome")
# else:
#      print("digit not palindrome")


# num2 = 153

# s_num2 =ste(num2)
# 1_num = len(s.num2)
# sum_num2 = 0
# for i in s_num:
#     sum_num2 + int(i**j_num2)

# print(sum_num2)

str1 = "welcome python"

s = str1.split() #['welcome, python']
print(s)

s.reverse() #['python','welcome']
print(s)

op_str = " ".join(s) #python welcome
print(op_str)