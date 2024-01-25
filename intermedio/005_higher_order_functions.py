### Higher order functions ###

from functools import reduce


def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_plus_one(value_1, value_2):
    return sum_one(value_1 + value_2)

print(sum_two_values_plus_one(5, 2))

def sum_two_values_plus_one(value_1, value_2, func):
    return func(value_1 + value_2)

print(sum_two_values_plus_one(5, 2, sum_one))
print(sum_two_values_plus_one(5, 2, sum_five))


# Closures

def sum_ten(init_value):
    def add(value):
        return value + 18 + init_value
    return add

add_closure = sum_ten(10)
print(sum_ten(10))
print(add_closure)
print(add_closure(5))
print(sum_ten(1)(2))


### Built-in Higher order functions ###

numbers = [2, 5, 10, 21, 3, 30]

# Map
def mul_2(numbers):
    return numbers * 2

print(numbers)
print(list(map(mul_2, numbers)))
print(list(map(lambda number: number * 5, numbers)))


# Filter

def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))


# Reduce

def sum_values(value_1, value_2):
    return value_1 + value_2

print(reduce(sum_values, numbers))







