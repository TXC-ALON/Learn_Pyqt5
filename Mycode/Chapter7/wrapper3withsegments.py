def outer(origin):
    def inner(*args, **kwargs):
        print("before")
        res = origin(*args, **kwargs)
        print(res)
        print("after")
        return res

    return inner


@outer
def func1(a1):
    print("func1")
    values = [1, 2, 3, 4, a1]
    return values


@outer
def func2(a1, a2):
    print("func2")
    m = [a1, a2]
    values = [1, 2, 3, 4, m]
    return values


@outer
def func3(a1, a2, a3):
    print("func3!!!")
    values = (1, 2, 3, 4)
    return a1 * a2 * a3


# func = outer(func)
result1 = func1(1)
result2 = func2(11, 22)
result3 = func3(5, 6, 8)
