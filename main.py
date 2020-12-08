# Simple password manager. This program is able to generate a new password or store a new account(name of the website, name, email, password)
# in a file, created by the program. This is not something advanced.

import random

print("Select what you want to do [1][2]")
print("[1] Generate a password")
print("[2] Store a new account")
choice = int(input())

while choice > 2 or choice < 1:
    print("Error please enter: 1 or 2")
    print("[1] Generate a password")
    print("[2] Store a new account")
    choice = int(input())

if choice == 1:
    n = 1
    password = ""
    char = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
    x = int(input("Enter the length of the password: "))
    for n in range(1,x):
        n += 1
        password += random.choice(char)
    print("Your randomly generated password is " + password)

elif choice == 2:
    website = str(input("Enter the name of the website:"))
    username = str(input("Enter the username on the website:"))
    email = str(input("Enter the email used on the website:"))
    print(" ")
    print("Do you want to generate a random password for your account?")
    print("[1] Generate a password for your account")
    print("[2] Enter your own password")
    choicepassword = int(input())
    while choicepassword > 2 or choicepassword < 1:
        print("Error please: 1 or 2")
        print("[1] Generate a password for your account")
        print("[2] Enter your own password")
        choicepassword = int(input())
    if choicepassword == 1:
        n = 1
        password = ""
        char = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
        x = int(input("Enter the length of your password: "))
        while (x<8):
            print("Your passwords needs to have more than 8 characters")
            x = int(input("Enter the length of your password:"))
        for n in range (1,x):
            password += random.choice(char)
            n += 1
        print("Your randomly generated password is " + password)
    elif choicepassword == 2:    
        password = str(input("Enter the password of the website:"))
        while len(password) < 8:
            print("Your passwords needs to have more than 8 characters")
            password = str(input("Enter the password of the website:"))

    f = open(website, "w")

    f.write ("Website name: " + website + "\n")
    f.write ("Username: " + username + " \n")
    f.write ("Email: " + email + " \n")
    f.write ("Password: " + password + "\n")
    f.close