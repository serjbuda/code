import string

a = string.printable
print(a)
b = a.replace("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",'')
print(b)
