import csv
import os
import sys
import getpass

light_blue = "\033[1;34m"
light_purple = "\033[1;35m"
light_green = "\033[1;32m"
light_red = "\033[1;31m"

print(light_blue, end="")
print("$$$ Login System $$$")


login = 'Y'
while login.upper() == 'Y':
    with open('data.csv', 'r', newline='') as file:
        reader = csv.reader(file, delimiter=',')
        rows = list(reader)
    
    found = False
    print(light_purple, end="")
    username = str(input("Enter Your User Name : "))
    password = str(getpass.getpass(prompt="Enter YOur Password : "))
    
    for row in rows:
        if len(row) != 0 and str(row[1]) == username and str(row[2]) == password:
            print(light_green, end="")
            print("You Login Succesfuly **")
            found = True
            break
    if not found:
        print(light_red, end="")
        print("Username OR Password Wrrong !")
    else:
        sys.exit()
    login = input("Try More Time (Y) No (Q) : ")
    if login.upper() == 'Q':
        login = 'Q'





