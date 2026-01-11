# Custom module examples


# import mymodule
# mymodule.greeting("sanjay")

# import mymodule as mx  # alias
# a = mx.person['age']
# print(a)

# from mymodule import person
# print(person['name'])


# Built-in module: platform

import platform

x = platform.system()
print(x)

x = dir(platform)
print(x)


# Custom calc module

# import calc
# print(calc.add(1, 6))


# Math module examples

import math

print(math.sqrt(4))

import math as m
print(m.sqrt(25))

from math import sqrt
print(sqrt(216))

from math import factorial
print(factorial(6))


# Random module

import random
print(random.randint(1, 5))


# __name__ == "__main__"

def test():
    print("hello")

if __name__ == "__main__":
    test()


# Lambda functions

add = lambda a, b: a + b
print(add(2, 6))

x = lambda a, b: a * b
print(x(2, 5))

x = lambda a, b, c: a + b + c
print(x(1, 2, 2))


def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(3)
print(mydoubler(11))


# map(), filter(), reduce()

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

numbers = [1, 2, 3, 4, 5, 6]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

from functools import reduce

nums = [1, 2, 3, 4]
total = reduce(lambda a, b: a + b, nums)
print(total)


# Sorting with lambda

students = [('emil', '22'), ('ram', '25'), ('shyam', '28')]
sorted_students = sorted(students, key=lambda x: x[0])
print(sorted_students)

words = ['sanjayana', 'aishekh', 'banana', 'cherry']
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)


# List Comprehension

numbers = [i for i in range(5)]
print(numbers)

squares = [x * x for x in range(1, 6)]
print(squares)

words = ['apple', 'banana', 'fruits']
lengths = [len(word) for word in words]
print(lengths)

names = ['sanjay', 'ram', 'hari']
upper = [name.upper() for name in names]
print(upper)

result = ['Even' if x % 2 == 0 else 'Odd' for x in range(6)]
print(result)


# Nested list comprehension

matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)


# Set comprehension

nums = [1, 2, 3, 4, 5]
unique = {x for x in nums}
print(unique)


# Conditional list comprehension

fruits = ['apple', 'banana', 'cherry', 'kiwi']
newlist = [x for x in fruits if 'i' in x]
print(newlist)
