# Diccionarios

my_dict = dict()
my_other_dict = {}
print(my_dict)
print(type(my_dict))
print(my_other_dict)
print(type(my_other_dict))

my_other_dict = {"Nombre": "Jialiang", "Apellido": "Ye", "Edad": 27, 1 : "Python"}
print(my_other_dict)

my_dict = {
    "Nombre": "Jialiang", 
    "Apellido": "Ye", 
    "Edad": 27, 
    "Lenguajes" : {"Python", "C", "C++", "Java"}
}
print(my_dict)
print(my_dict["Nombre"])
my_dict["Nombre"] = "Jordi"
print(my_dict["Nombre"])
print(my_dict["Lenguajes"])
my_dict["Direccion"] = "c/ lkdshfaljdkflasjdlasjd"
print(my_dict)

del my_dict["Direccion"]
print(my_dict)
del my_dict
#print(my_dict)

my_dict = {
    "Nombre": "Jialiang", 
    "Apellido": "Ye", 
    "Edad": 27, 
    "Lenguajes" : {"Python", "C", "C++", "Java"}
}
print("Jialiang" in my_dict)
print("Jia" in my_dict)
print("Nombre" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
print(my_dict.fromkeys(("Nombre", "Lenguajes")))

my_other_new_dict = my_dict.fromkeys(("Nombre", "Lenguajes"))
print(my_other_new_dict)

my_list = ["Nombre", 1, "Piso"]
my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)
my_new_dict = dict.fromkeys((my_dict))
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict, ("Jialiang", "Ye"))
print(my_new_dict)
#my_new_dict = dict.fromkeys(my_dict, "Jialiang", "Ye")
#print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict, ["Jialiang", "Ye"])
print(my_new_dict)

print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))
print(my_new_dict)
print(my_dict.values())
print((dict.fromkeys(list(my_new_dict.keys()))))
print((dict.fromkeys(list(my_other_dict.values()))))
