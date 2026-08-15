person = {
    "name": "Alex",
    "age": 20,
    "city": "Cologne"
}

print(person["name"])

# Safer lookup
print(person.get("name"))

# Add
person["job"] = "Programmer"

# Change
person["age"] = 21

# Delete
del person["city"]

# Loop
for key, value in person.items():
    print(key, value)
