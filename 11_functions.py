def greet():
    print("Hello!")


greet()


def greet_person(name):
    print(f"Hello, {name}!")


greet_person("Alex")


def add(a, b):
    return a + b


result = add(10, 20)

print(result)


# Default argument

def greet(name="World"):
    print(f"Hello, {name}!")


greet()
greet("Alex")


# *args

def add_many(*numbers):
    return sum(numbers)


print(add_many(1, 2, 3, 4, 5))


# **kwargs

def show_info(**info):
    print(info)


show_info(name="Alex", age=20)
