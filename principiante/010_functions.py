# Funciones

def my_function():
    print("Esto es una función")

my_function()


def sum_two_values(first_value, second_value):
    print(first_value + second_value)

sum_two_values(10, 11)
sum_two_values("10", "11")


def sum_with_return(first_value, second_value):
    return first_value + second_value

result = sum_with_return(10,11)
print(result)


def print_name(name, surname):
    print(f"{name} {surname}")

print_name("Jialiang", "Ye")
print_name(surname = "Ye", name = "Jialiang")


def print_name_with_default(name, surname, alias = "Sin alias"):
    print(f"{name} {surname}, alias: {alias}")

print_name_with_default("Jialiang", "Ye")
print_name_with_default("Jialaing", "Ye", "Lele")


def print_text(*text):
    print(text)

print_text("Hola", "que", "tal, como", "te llamas. Mi nombre es Jialiang")


def print_upper_text(*text):
    for element in text:
        print(element.upper())

print_upper_text("Hola", "que", "tal, como", "te llamas. Mi nombre es Jialiang")
