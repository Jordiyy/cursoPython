# Bucles

# while
my_condition = 0
while my_condition < 10:
    print(my_condition)
    my_condition += 1
if my_condition == 10:
    print("La condicion tiene el valor 10")
else:
    print("La condicion del bucle while ya o se cumple")

print("Termina el bucle while")

my_condition = 0
while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        break
    print(my_condition)

print("Termina el bucle while")

#for
my_list = [35, 24, 62, 52, 30, 30, 17]
for element in my_list:
    print(element)
print("Termina bucle for")

my_number = 12
for number in range(my_number):
    print(number)
print("Termina bucle for 2")

my_tuple = [27, 1.70, "Jialliang", "Ye", "Ye"]
for element in my_tuple:
    print(element)
print("Termina bucle for 3")

my_set = {"Jialliang", "Ye", "Ye"}
print(my_set)
for element in my_set:
    print(element)
print("Termina bucle for 4")

my_dict = {"Nombre": "Jialliang", "Apellidos": "Ye", "Edad": 27}
for element in my_dict:
    print(element)
print("Termina bucle for 5")
for element in list(my_dict.values()):
    print(element)
print("Termina bucle for 6")











