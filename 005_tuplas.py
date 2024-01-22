# Tuplas

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (27, 1.77, "Jialiang", "Ye", "Ye")
my_other_tuple = (10, 20, 30 ,40 ,50)

print(my_tuple)
print(my_tuple.count("Ye"))
print(my_tuple.index(27))
#my_tuple[0] = 20

print(my_tuple + my_other_tuple)

my_new_tuple = list(my_tuple)
my_new_tuple.append(100)
print(tuple(my_new_tuple))

del my_new_tuple
#print(my_new_tuple)













