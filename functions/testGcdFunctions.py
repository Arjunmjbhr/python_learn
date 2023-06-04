from gcdFunction import gcd

# prompt user to enter 2 integers

n1 = eval(input("enter the first integer: "))
n2 = eval(input("enter the second integer: "))

print("the greatest common divider for", n1, "and", n2, "is", gcd(n1,n2))