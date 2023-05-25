import functools

def auth(func):
    @functools.wraps(func)
    def inner(*args,**kwargs):
        """ inner comments"""
        print("hello")
    return inner
@auth
def admin():
    """good good study"""

    print("hello")
@auth
def admin2():
    """day day up"""

    print("hello")




print(admin.__name__)
print(admin.__doc__)
print(admin2.__name__)
print(admin2.__doc__)
