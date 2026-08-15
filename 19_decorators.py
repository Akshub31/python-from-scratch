def my_decorator(function):

    def wrapper():
        print("Before function")
        function()
        print("After function")

    return wrapper


@my_decorator
def hello():
    print("Hello!")


hello()
