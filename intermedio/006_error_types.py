### Error types ###


# SyntaxError
#print "Hola mundo" #Error
print("Hola mundo")


# NameError
#print(name) # Error
name = "Hola"
print(name)


# IndexError
list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(list[1])
print(list[4])
#print(list[5]) # Error


# ModuleNotFoundError
#import maths   # Error
import math


# AttributeError
#print(math.PI) # Error
print(math.pi)


# KeyError
dict = {"Nombre": "Jialiang", "Apellido": "Ye", "Edad": 27, 1: "Python"}
#print(dict["Apelido"])
print(dict["Apellido"])


# TypeError
list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
#print(list["Python"])  # Error
print(list[0])


#ImportError
#from math import PI    # Error
from math import pi


# ValueError
my_int = int("10")
#my_int = int("10 años")    # Error
print(type(my_int))

# ZeroDivisionError
print(4/2)
#print(4/0) # Error