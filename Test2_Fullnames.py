fname = input("Enter your first name: ")
lname = input("Enter your last name: ")           
age = int(input("Enter your age: "))
yeaOfBirth = int(input("What year were you born? "))
fullname = fname +"  "+ lname 

print("Your fullname is " + fullname )
print(f"Your name and your {age} years of age is... not weird at all, dude")

age += yeaOfBirth
newAge = age
print(f"Your age this year plus your Year of Birth is {newAge}, and it is this year's date... ha!")    
      
