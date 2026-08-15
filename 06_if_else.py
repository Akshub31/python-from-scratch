age = 18

if age >= 18:
    print("Adult")
else:
    print("Minor")


score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("Fail")


# Logical operators

age = 20
has_id = True

if age >= 18 and has_id:
    print("Allowed")

if age < 18 or not has_id:
    print("Not allowed")
