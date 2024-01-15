# A Program that allows for input of of two numbers, and prints the swap of the input

a = input("Enter an initial value: ")
b = input("Enter the next value: ")

# creating new variables for the swap

# I had to think of a 'third cup' to hold the value of one of the variables'
input1 = a
a = b
b = input1

print("The swapped is \n" + "______________")
print("Initial value: " + a)
print("Next value: " + b)
