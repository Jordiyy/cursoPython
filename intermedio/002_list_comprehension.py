###   List comprehension  ###

original_list = [35, 24, 62, 52, 30, 30, 17]
my_list = [element for element in original_list]
print(my_list)

my_list = [element for element in range(10)]
print(my_list)

my_list = [element + 10 for element in range(10)]
print(my_list)

my_list = [element * element for element in range(10)]
print(my_list)

def sum_five(number):
    return number + 5

my_list = [sum_five(element) for element in range(10)]
print(my_list)
