###   Challenges  ###

#   FIZZ BUZZ
"""
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
 - Múltiplos de 3 por la palabra "fizz".
 - Múltiplos de 5 por la palabra "buzz".
 - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizzbuzz():
    for numero in range(1,101):
        if numero % 3 == 0 and numero % 5 == 0:
            print('fizzbuzz')
        elif numero % 3 == 0:
            print('fizz')
        elif numero % 5 == 0:
            print('buzz')
        else:
            print(f'{numero}')

fizzbuzz()


# Anagrama
"""
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
 - Un Anagrama consiste en formar una palabra reordenando TODAS
   las letras de otra palabra inicial.
 - NO hace falta comprobar que ambas palabras existan.
 - Dos palabras exactamente iguales no son anagrama.
"""

def is_anagram(first_word, second_word):
    if first_word.lower() == second_word.lower():
        return False
    return sorted(first_word.lower()) == sorted(second_word.lower())

print(is_anagram("amor", "roma"))
print(is_anagram("AMOR", "roma"))
print(is_anagram("AMOR", "amor"))


# Fibonacci
"""
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
 - La serie Fibonacci se compone por una sucesión de números en
   la que el siguiente siempre es la suma de los dos anteriores.
   0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci():
    list_fibonacci = []
    index_fibonacci = 0

    for index in range(51):
        if len(list_fibonacci) < 2 :
            list_fibonacci.append(index_fibonacci)
            index_fibonacci += 1
        else:
            index_fibonacci = list_fibonacci[-1] + list_fibonacci[-2]
            list_fibonacci.append(index_fibonacci)

    print(list_fibonacci)

fibonacci()


# Numero primo
"""
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""

def is_primo(num_to_check):
    list_primo = []
    for index in range(101):
        if index == 1:
            list_primo.remove(0)
        else:
            bool_primo = True
            for numero in list_primo:
                if numero != 1 and index % numero == 0:
                    bool_primo = False
            if bool_primo == True:
                list_primo.append(index)

    if num_to_check in list_primo:
        print(f'El número {num_to_check} es primo')
    else:
        print(f'El número {num_to_check} no és primo')
    
    print(list_primo)
            
is_primo(64)


# Invertir cadenas
"""
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def invert(string):
    inverse_text = ""
    inverse_length = len(string)
    print(string)
    for position in range(len(string)):
        inverse_text += string[inverse_length - position - 1]
    print(inverse_text)

invert("Hola mundo")
