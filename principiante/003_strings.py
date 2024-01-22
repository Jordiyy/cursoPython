# Strings

my_string = "Este es mi string"
my_other_string = 'Este es otro string diferente'

print(len(my_string))
print(len(my_other_string))

my_new_string = "Este es un string con \n un salto de linea."
my_tab_string = "Este es un string con \t tabulacion."
my_combined_string = "\tEste es un string con una combinacion de \n salto de linea con tabulacion al inicio."
my_string_ignorado = "\\t Este string ignora tabulaciones y \\n saltos de linea."

print(my_new_string)
print(my_tab_string)
print(my_combined_string)
print(my_string_ignorado)

name, surname, age = "Jialiang", "Ye", 27
print("Mi nombre es {} {} y tengo {} años.".format(name, surname, age)) # Menos recomendable
print("Mi nombre es %s %s y tengo %d años." %(name, surname, age)) # Recomendable
print("Mi nombre es " + name + " " + surname + " y tengo " + str(age) + " años.") # No recomendable
print(f"Mi nombre es {name} {surname} y tengo {age} años.") #Recomendable

# Desempaquetado de caracteres
language = "python"
a,b,c,d,e,f = language
print(a)
print(f)

# Division 
language_slice = language[1:3]
print(language_slice)
language_slice = language[1:]
print(language_slice)
language_slice = language[-2]
print(language_slice)
language_slice = language[0:6:2]
print(language_slice)

# Reverse
reverse_language = language[::-1]
print(reverse_language)

# Funciones
print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.upper().isupper())
print(language.lower().isupper())
print(language.startswith("Py"))
print(language.startswith("py"))
print(language.startswith("tho"))
