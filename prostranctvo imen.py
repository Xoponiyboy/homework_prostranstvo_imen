import math

def square(x):
    global a
    a = x ** 2
    # print(globals())
    # print(locals())
    return a

a = 5
b = square(2)
print(a)
print(b)
print(globals())