### Listas ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [27, 1.77, "Jialiang", "Ye"]

print(my_other_list)
print(type(my_other_list))
print(my_other_list[0])
print(my_other_list[-1])
print(my_other_list[-4])
#print(my_other_list[-5])
print(my_other_list[3])
#print(my_other_list[4])
print(my_other_list.count("Jialiang"))

age, height, name, surname = my_other_list
print(name)

print(my_list + my_other_list)


print(my_list)
my_list.append(50)
print(my_list)
my_list.insert(1, 10)
print(my_list)
my_list.remove(50)
print(my_list)
my_list.remove(my_list[1])
print(my_list)
my_pop_element = my_list.pop()
print(my_pop_element)
print(my_list.pop())
print(my_list)
del my_list[2]
print(my_list)
my_list[2] = 100
print(my_list)
my_copied_list = my_list.copy()
my_list.clear()
print(my_list)
print(my_copied_list)
my_copied_list.reverse()
print(my_copied_list)
my_copied_list.sort()
print(my_copied_list)


# Tipos dinámicos
my_list = "Hola Python"
print(my_list)
