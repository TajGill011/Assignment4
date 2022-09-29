#Revision number 1 
#Sartaj Gill 09/27/2022

a = input("Please enter a string:\n") #Stores the user input as A
print(f"\033[1;31;40m{a}") #Prints the user input in the color red.\003[ is the escape code. 1 for the style, 31 for the color red and 40m for the background color black
print(f'\033[0;37;40mYou entered "{a}" and its type is {type(a)}') #Prints what the user entered as the input in white and its type
b = input("Please enter a integer:\n") #Stores the user input as B
print(f"\033[1;31;40m{b}") #Prints the user input
print(f'\033[0;37;40mYou entered "{b}" and its type is {type(b)}')#Prints what the user entered as the input in white and its type

#Revision number 1 09/27/2022
#End Sartaj Gill 