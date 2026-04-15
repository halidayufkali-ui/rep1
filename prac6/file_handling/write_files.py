# File modes: w, a, x

# Write (overwrites file)
with open("example.txt", "w") as file:
    file.write("Hello World\n")
    file.write("Practice 6\n")

# Append (adds to file)
with open("example.txt", "a") as file:
    file.write("Appended line\n")

