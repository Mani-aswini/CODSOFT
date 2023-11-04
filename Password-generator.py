#PASSWORD_GENERATOR_PYTHON

import random

letters = ["a","b,","c,","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
Symbols = ["!","@","#","$","%","^","&","*","(",")"]


no_of_letters = int(input("Enter the numbers of letters: \n"))
no_of_numbers = int(input("Enter the number of numbers: \n"))
no_of_symbols = int(input("Enter the number of symbols: \n"))

password = ""

for i in range(0,no_of_letters):
    password = password + random.choice(letters)
    #print(password)

for i in range(0,no_of_numbers):
    password = password + random.choice(numbers)
    #print(password)


for i in range(0, no_of_symbols):
    password = password + random.choice(Symbols)
    #print(password)

print(f"your simple password is: {password}")
