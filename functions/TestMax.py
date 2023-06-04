def max(num1, num2):
    if num1 > num2:
        result = num1
    else:
        result = num2
    return result

def main():
    i = eval(input("Give the value for Num1: "))
    j = eval(input("Give the value for Num2: "))
    k = max(i, j) # call the max function
    print("The larger number in", i , "and", j, "is", k)

main() # call the function 
