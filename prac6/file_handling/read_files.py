# File modes: r
# Reading files: read(), readline(), readlines()

with open("example.txt", "r") as file:
    content = file.read()
    print("Using read():")
    print(content)

with open("example.txt", "r") as file:
    print("\nUsing readline():")
    print(file.readline())

with open("example.txt", "r") as file:
    print("\nUsing readlines():")
    lines = file.readlines()
    for line in lines:
        print(line)