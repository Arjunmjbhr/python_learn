from random import randint # import random int

# Generate a random character between ch1 and ch2
def getRandomCharacter(ch1, ch2):
    return chr(randint(ord(ch1), ord(ch2)))

# Generate a random lower case letter 
def getRandomLowerCaseLetter():
    return getRandomCharacter('a', 'z')

# Generate a random Upper case Letter 
def getRandomUpperCaseLetter():
    return getRandomCharacter('A', 'Z')

# Generate a random Digit Character 
def getRandomDigitCharacter():
    return getRandomCharacter('0', '9')


# Generate a random character
def getRandomASCIICharacter():
    return chr(randint(0 , 127))

def main():
    ch1 = str(input("Enter Ch1: "))
    ch2 = str(input("Enter ch2: "))
    print(getRandomCharacter(ch1,ch2))
    print(getRandomLowerCaseLetter())
    print(getRandomUpperCaseLetter())
    print(getRandomDigitCharacter())
    print(getRandomASCIICharacter())
    
main()