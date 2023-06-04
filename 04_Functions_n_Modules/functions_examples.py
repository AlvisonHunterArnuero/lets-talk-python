# Basic Function definitions
from string_operations import reverse_string
from basic_operations import add
import datetime
import math
import random


def greet(name):
    print("Hello, " + name + "!")


# Calling the function
greet("Alvison")


def add_numbers(a, b):
    return a + b


# Calling the function and storing the result in a variable
result = add_numbers(5, 3)
print(result)

# Using parameters to be used inside the function
# We can define some optional params by adding a default value


def user_name(name: str, last_name: str = '') -> str:
    return f'{name: str} {last_name}'


# Calling the function with some of the params not included
admin = user_name('Alvison')
print(f'Admin is {admin}')

instructor = user_name('Alex', 'Ruiz')
print(instructor)


# Built-in functions for Python - Examples
text = "Python is simply awesome!"
length = len(text)
print(length)

# Combining built-in functions with some imported modules functions
random_number = random.randint(1, 10)
print(random_number)

# A second example of this, importing the math module to our file

number = 16
sqrt = math.sqrt(number)
print(sqrt)

# A third example using date and time module in our import to this file

current_time = datetime.datetime.now()
print(current_time)

# Using custom modules
# Importing and using the custom module basic_operations.py in our file:
result = add(3, 4)
print(result)

# Another example of custom module, imported from string_operations.py
print(reverse_string("Hablemos Python!"))

# using anonymous functions or lambda as they are called in Python


def greet(name): return "Hello, " + name + "!"


# Calling the lambda function
print(greet("Alvison"))
