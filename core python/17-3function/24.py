"""
1)nested function:>it means the the function call inside the function ,inner functionn ko call krne ke liye outer function ko call krna pdta hai.
2)closures:> it is a kind of nestead function.
3)decorates:>
"""

#nested function
# def outerfun():

#     def innerfunc():
#         data=1234
#         print(data)
#     innerfunc()
# outerfun()
# #op=1234

# def outer():
#     def inner():
#         x=1234
#         print(x)

# print("caalling outeer function from the global scope")
# outer()
# op=caalling outeer function from the global scope

# print("Hello All")

# def outer():
#     print("start of outer function")
#     def inner():
#         x=1234
#         print(x)

#     inner()
#     print("end of outer function")

# print("calling outer function of global scope")
# outer()
# print("bye bye")
# op=calling outer function of global scope
# start of outer function
# 1234
# end of outer function
# bye bye
 

#NESTED FUNCTION->CLOSURES->DECORATORS
# def outer(v1):
#     print("start of outer function")
    
#     def inner():
#         X=1234
#         print(x + v1)

#     inner()
#     print("end of outer function")

# print("calling outer function of global scope")
# outer(23)
# print("bye bye")

# op=calling outer function of global scope
# start of outer function
# 1257
# end of outer function
# bye bye

# def outer(v1):
#     print("start of outer function")
    
#     def inner(X):
       
#         print(X + v1)

#     inner(12)
#     print("end of outer function")

# print("calling outer function of global scope")
# outer(23)
# print("bye bye")

# op=calling outer function of global scope
# start of outer function
# 35
# end of outer function
# bye bye


def outer(x):
    def inner():
        return x + 2
    return inner
outer(10)
res=outer(10)
print(res)
print(type(res))
