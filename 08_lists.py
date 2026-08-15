fruits = ["apple", "banana", "orange"]

print(fruits)

print(fruits[0])
print(fruits[-1])

fruits.append("grape")
fruits.insert(0, "mango")

fruits.remove("banana")

last = fruits.pop()

print(fruits)
print(last)

print(len(fruits))

for fruit in fruits:
    print(fruit)

# Sort
numbers = [5, 2, 8, 1, 3]

numbers.sort()

print(numbers)
