#Revision number 1 
#Sartaj Gill 09/27/2022
 
e = input("Do you want to add a dinner guest? (Enter anything to continue, enter end to end") #Asks user if they want to add a guest to the dinner list
print("Dinner List\n") #Prints Dinner List as a title for the outputs to come underneath
while e == 'continue': #While loop for the loop to be continous
    k = input("Do you want to add a dinner guest? (Enter continue to continue, enter end to end") #Asks the user each time if they want to continue
    if k == 'end':#if the user input is end then it ends the program
        quit()
    a = input("Enter the first and last name of the guest: ") #Asks user for the name
    b = input("Enter the date you invited the guest(format mm/dd/yyyy): ") #Asks user for their invitation date for the person
    DinnerGuests = [x+y for x in [f"{a} "] for y in [f"invited on {b}"]] #list comprehension, conjoins users input for name and invitation date into one entry
    print(DinnerGuests) #Prints the list

#Revision number 1 09/27/2022
#End Sartaj Gill 