import json

person = {
    "name": "Alex",
    "age": 20,
    "skills": ["Python", "Git"]
}

# Python -> JSON
json_data = json.dumps(person)

print(json_data)

# JSON -> Python
data = json.loads(json_data)

print(data["name"])
