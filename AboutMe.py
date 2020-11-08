import datetime

print('Hello, this is a simple Python code!')
print("")
print('Here\'s a picture of a cat:')
print("")
print("|\---/|")  
print("| ,_, |")
print(" \_`_/-..----.")
print(" ___/ `   ' ,""+ \ ")
print("(__...'   __\    |`.___.';")
print(" (_,...'(_,.`__)/'.....+")
print("")
print("I live in Milan")
print("")
print("         '::.")
print("    _________H ,%%&%,")
print("   /\     _   \%&&%%&%")  
print("  /  \___/^\___\%&%%&&") 
print("  |  | []   [] |%\Y&%'") 
print("  |  |   .-.   | ||  ")  
print("~~@._|@@_|||_@@|~||~~~~~~~~~~~~~")
print("         ) )")
print("")
born = input("What year you were born? ")

while born>=2020:
    born = input("Error! Insert another year: ")
        
born = int(born)
now = datetime.datetime.now()
age = now.year - born
print("You have: " + str(age) + " years old.")

if age <= 0:
    catAge = 0        
if age == 1:
    catAge = 15        
if age == 2:
    catAge = 24        
if age > 2:
    catAge = (age -2 )*4 + 24

print("If you were a cat you would have: " + str(catAge))
