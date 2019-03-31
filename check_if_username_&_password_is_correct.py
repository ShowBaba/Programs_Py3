my_username = 'Sammy'
my_password = 1234

username = input("Input Username:")

if username != my_username:
    print("Incorrect username X")
else: 
    password = int(input("Input Password:"))

    if password == my_password:
        print("You are now logged in! ")
    else:
        print("Incorrect Password X")
    
