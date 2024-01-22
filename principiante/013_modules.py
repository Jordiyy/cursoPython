# Modulos
import module
module.sum(1,7,2)
module.print_value("Hola, Jordi")

from module import sum, print_value
sum(10,5,35)
print_value("No es necesario llamar el nombre del modulo si se importa como objeto")

import math
import random

print(math.pi)
print(math.pow(2, 4))

from math import pi as PI_VALUE

print(PI_VALUE)






