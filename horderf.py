def my_decorator(func):
    def wrapper():
        print("Inside the Decorator")
        # print(func.__name__)
        func()

    return wrapper


@my_decorator
def my_function():
    print("I'm running...")


my_function()


li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(filter(lambda x: (x % 2 != 0), li))
print(final_list)


x = lambda a: a + 10
print(x(5))
