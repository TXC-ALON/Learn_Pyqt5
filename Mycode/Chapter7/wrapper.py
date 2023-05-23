def func():
    print("hello")
    values = (1, 2, 3, 4)
    return values


def outer(origin):
    def inner():
        return origin()
    return inner


func = outer(func)
result = func()
print(result)
