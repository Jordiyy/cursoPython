# Variables

my_string_variable = "Mi variable de tipo string"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)

print(my_int_variable)
my_int_to_str_variable = str(my_int_variable)
print(type(my_int_to_str_variable))

# Concatenación de variables de diferentes tipos
print(my_string_variable, my_int_variable, my_bool_variable)
print("Este es el valor guardado en my_int_varaible: ", my_int_variable)


# Algunas funciones del sistema
print(len(my_string_variable))
print(len(my_int_to_str_variable))

# Varables en una sola linea, no recomendable. Mejor en lineas separadas.
name, surname, age = "Jialiang", "Ye", 27
print("Mi nombres es ", name, surname, "y tengo ", age, "años.")

# Inputs de variables
first_name = input("¿Cómo te llamas? ")
age = input("¿Cuántos años tienes? ")

print("Así que, te llamas ", first_name, "y tienes", age, "años.")

# Forzar el tipo de la variable, tiene sentido en inputs pero no en outputs porque puede variar luego
address: str = "Mi dirección de casa."
print(address)
print(type(address))
address = 27
print(address)
print(type(address))


