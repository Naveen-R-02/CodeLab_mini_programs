import os
path = input("Enter the path of the file: ")
count = 0
for file in os.listdir(path):
    if file.endswith(".py"):
        count += 1

print(".py files in the directory:", count)