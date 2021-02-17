print("Hello and welcome to the Text Files R' Us!")
print("We will Read or Write text files for you!")
answer = input("What do you wanna do? ") # It's Input 

if answer == "Read": # Checks if "Read" is exactly what was typed
    swag = open("supercalifragilisticexpialidocious.txt", "r") # open's the file to be edited
    print(swag.read()) # prints the file's contents
    swag.close() # closes the file so it can be used the next time

elif answer == "Write": # Checks if "Write" is exactly what was typed
    pog = input("Okie Dokie! ") 
    leg = open("supercalifragilisticexpialidocious.txt", "wt")
    leg.write(pog) # either put a or w, a will add, w will overwrite everything. We will use "w"
    leg.close() # closes the file so it can be used the next time