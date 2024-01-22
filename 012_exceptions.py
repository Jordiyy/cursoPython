# Manejo de excepciones

value_one = 5
value_two = 1
print(value_one + value_two)

value_two = "1"

try:
    print(value_one + value_two)
except:
    print("No se puede realizar la operación")


value_two = 1
try:
    print(value_one + value_two)
except:
    print("No se puede realizar la operación")
else:
    print("La ejecución continua")


value_two = "1"
try:
    print(value_one + value_two)
except:
    print("No se puede realizar la operación")
else:
    print("La ejecución continua")
finally:
    print("Se ejecuta código")


value_two = 1
try:
    print(value_one + value_two)
except:
    print("No se puede realizar la operación")
else:
    print("La ejecución continua")
finally:
    print("Se ejecuta código")


#Excepciones por tipo
value_two = "1"
try:
    print(value_one + value_two)
except TypeError:
    print("No se puede realizar la operación por un error de tipo TypeError")
except ValueError:
    print("Se ha producido un error de tipo ValueError")

#Captura de la información
try:
    print(value_one + value_two)
except ValueError as e:
    print("Se ha producido un error de tipo ValueError")
    print(e)
except Exception as random_name:
    print(random_name)
  
