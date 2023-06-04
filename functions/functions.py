from math import *

def calculateArea(radius):
    area = pi * pow(radius,2)
    
    return area

r = 2
x = calculateArea(r)
print(x)

j = 5 
y = calculateArea(j)
print(y)

print(len("Hello World.."))

def customLength(s):
    count = 0
    for ch in s:
        count += 1
    return count

simpleString = "hello python!.."
y = customLength(simpleString)
print(y)
        