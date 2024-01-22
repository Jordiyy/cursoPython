### SETS ###

my_set = set()
my_other_set = {}

print(my_set)
print(type(my_set))
print(my_other_set)
print(type(my_other_set))

my_other_set = {"Jialiang", "Ye", 27}
print(my_other_set)
print(type(my_other_set))
print(len(my_other_set))

my_other_set.add("Lele")
print(my_other_set)
my_other_set.add("Lele")
print(my_other_set)

print("Ye" in my_other_set)
print("Yan" in my_other_set)

my_other_set.remove("Lele")
print(my_other_set)

my_other_set.clear()
print(my_other_set)

my_other_set = {"Jialiang", "Ye", 27}
print(my_other_set)
del my_other_set
#print(my_other_set)

my_set = {"Jialiang", "Ye", 27}
my_list = list(my_set)
print(my_list)

my_other_set = {"C", "C++", "Java", "Python"}
print(my_other_set.union(my_set).union({"PHP", "javascript"}))
my_new_set = my_other_set.union(my_set)
print(my_new_set)

print(my_new_set.difference(my_set))

