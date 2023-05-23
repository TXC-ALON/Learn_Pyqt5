def outer(origin):
    def inner():
        print("before")
        res = origin()
        print("after")
        return res

    return inner


@outer
def func():
    print("hello")
    values = (1, 2, 3, 4)
    return values


# func = outer(func)
result = func()
print(result)
