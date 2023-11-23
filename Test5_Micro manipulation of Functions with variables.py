#another test of functions, but this time, it returns an output and stores it
#interesting to note; unless converted to numbers, all inputs are treated as strings and concantenated

def addIns():
    num1 = int(input('Enter a number between 1 and 10: '))
    num2 = int(input('Enter a number between 20 and 40: '))

    return num1+num2

print(f"The Additions of the entered rumbers are ", addIns())
