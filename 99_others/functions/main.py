from cryptography.fernet import Fernet

def isEven(n):
    return n % 2 == 0

def double(n):
    return n*2

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter
# for i in filter(isEven, x):
#     print(i)

# # Map
# for i in map(double, x):
#     print(i)

# Binary version of an integer
# print(bin(36))

# Returns the boolean value of the specified object
# print(bool("hola"))

# def f(*args):
#     for elem in args:
#         print(elem)

# f(1, 2, 4, "hola")

# Returns an array of bytes (integers)
print(bytes("Hola mundo",'utf-8'))

