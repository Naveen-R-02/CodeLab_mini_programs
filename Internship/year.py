name = input("Enter your name: ")
year = input("Enter your birth year: ")

common = ["123","1234","@123","13579","admin","qwerty"]
chars = "!@#$%^&*()"

for c in common:
    print(name + year + c)
    print(name + year + chars)
    print(name.capitalize() + c)
