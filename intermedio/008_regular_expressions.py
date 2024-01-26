### Regular expressions ###

import re

my_string = "Esta es la leccion 008 de Python. Las expresiones regulares."
my_other_string = "Esta no es la lección que toca. La Lección es la anterior"

match = re.match("Esta es la leccion", my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])

match = re.match("Esta es la leccion", my_other_string)
if match != None:
    print(match)
    start, end = match.span()
    print(my_string[start:end])

print(re.match("Esta es la leccion", my_other_string))
print(re.match("las expresiones", my_string))


# search
print(re.search("Esta es la leccion", my_string, re.I))
print(re.search("Python", my_string, re.I))


# findall
print(re.findall("la", my_string))
print(re.findall("la", my_string, re.I))


# split
print(re.split(" ", my_string))


# sub
print(re.sub("expresiones", "Expresiones", my_string))
print(re.sub("expresiones", "exp", my_string))
print(re.sub("[lección|L]ección", "LECCIÓN", my_other_string))
print(re.sub("[l|L]ección", "LECCIÓN", my_other_string))


# Patterns
pattern = r'[l|L]ección'
print(re.findall(pattern, my_other_string))

pattern = r'[l|L]ección|no'
print(re.findall(pattern, my_other_string))

pattern = r'[0-5]'
print(re.findall(pattern, my_string))

pattern = r'[0-9]'
print(re.findall(pattern, my_string))

pattern = r'\d'
print(re.findall(pattern, my_string))

pattern = r'\D'
print(re.findall(pattern, my_string))

pattern = r'[l].'
print(re.findall(pattern, my_string))

pattern = r'[l].*'
print(re.findall(pattern, my_string))




