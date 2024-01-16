#1. Create a greeting for your program.

#2. Ask the user for the city that they grew up in.

#3. Ask the user for the name of a pet.

#4. Combine the name of their city and pet and show them their band name.

#5. Make sure the input cursor shows on a new line:

# Start of Code - Project 

print("Hey, " + input("Enter Player Name to Start: ") + "!" + "\n Welcome to the Ban Name Generator!")

city = input("In what city were you born? ")

pet = input("What is your favorite animal? ")

bandName = city + " " + pet

print("Check this... but, you could create a band with the name \n" + bandName + ", 😏")