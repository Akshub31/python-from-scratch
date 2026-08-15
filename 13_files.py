# Write

with open("data.txt", "w") as file:
    file.write("Hello Python!\n")
    file.write("Learning files.")


# Read

with open("data.txt", "r") as file:
    content = file.read()

print(content)


# Append

with open("data.txt", "a") as file:
    file.write("\nNew line.")
