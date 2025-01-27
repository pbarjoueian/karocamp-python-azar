from math import floor
from pprint import pprint
from datetime import datetime

# import math


# print("What's your name?")
# name = input()
# print("Nice to meet you, " + name)

# # determine the length of the name
# name_length = len(name)
# print(name_length)

# print("Whats your birth year?")
# birth_year = input()
# age = 2024 - int(birth_year)
# print(age)


# print(math.floor(4.9))

# print(floor(4.9))


# persons = [
#     {"name": "John", "age": 30},
#     {"name": "Jane", "age": 25},
#     {"name": "Bob", "age": 35},
# ]
# pprint(persons)


# print(datetime.now().year)

# file = open("message.txt", "w", encoding="utf-8")
# file.write("hello\n")
# file.write("world\n")
# file.close()


# import urllib.request

# # make a HTTP request
# req = urllib.request.urlopen("https://en.wikipedia.org")
# # read content as utf-8 string
# content = req.read().decode("utf-8")

# # save to file
# file = open("wikipedia.html", mode="w", encoding="utf-8")
# file.write(content)
# file.close()


# import random

# # print(random.randint(1, 6))
# coin = ["heads", "tails"]
# print(random.choice(coin))


# names = ["Alice", "Bob", "Charlie"]

# for name in names:
#     print("Hello " + name + "!")

# for i in range(10):
#     print(i)


# a = 1

# while a < 2000:
#     print(a)
#     a = a * 2


# a = 1

# while True:
#     a = a * 2
#     print(a)
#     # if (a > 1000):
#     #     break


# def average(a, b):
#     result = (a + b) / 2
#     print(result)
#     return result


# x = average(2, 5)

# print(result)


m = "Hello, world"


def average(a, b):
    m = (a + b) / 2
    return m


x = average(1, 2)

print(m)  # prints "Hello, world"
