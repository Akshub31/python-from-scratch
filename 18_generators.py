def numbers():
    for i in range(5):
        yield i


for number in numbers():
    print(number)
