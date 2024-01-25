### Lambda  ###

sum_two_values = lambda first_value, second_value: first_value + second_value
print(sum_two_values(2, 4))
print(sum_two_values)

sum_two_values = lambda first_value, second_value: print(first_value + second_value)
print(sum_two_values(2, 4))


multiply_values = lambda first_value, second_value: first_value * second_value - 3
print(multiply_values(2, 4))

def sum_three_values(number):
    return lambda first_value, second_value: first_value + second_value + number

print(sum_three_values(5)(2,4))
