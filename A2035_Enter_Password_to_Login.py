#While Loop with Password

correct_password = "python123"
password = input("Enter a password:    ")
while correct_password != password:
    password = input("Wrong Password ! Try Again,\nEnter Password:    ")
    
print("Logged IN")
