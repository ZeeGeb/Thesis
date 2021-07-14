a = "Operations "
b = "Research "
c = "344"
d = a +b+c
print(d)

name = input("Please enter your name ")
age = int(input("Please enter your age "))

print("{} is {} years old".format(name,age))

def func(a,b):
    ssum = a+b
    diff = a-b
    prod = a*b
    quot = a/b
    
    return ssum,diff,prod,quot