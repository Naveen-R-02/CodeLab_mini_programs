password = input("Enter your password: ")

if len(password) < 8:
    print("Password isn't lengthy enough")
else:
    print("Password is strong")