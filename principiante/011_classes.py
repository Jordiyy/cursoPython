# Classes

class MyEmptyPerson:
    pass

class MyPerson:
    def __init__(self, name , surname):
        self.name = name
        self.surname = surname
        self.full_name = f"{name} {surname}"

    def walk(self):
        print(f"{self.full_name} está caminando")

my_person = MyPerson("Jialiang", "Ye")
print(my_person)
print(my_person.name)
print(f"{my_person.name} {my_person.surname}")
print(my_person.full_name)

my_person.walk()
my_person.full_name = "Jialiang Ye Yan (Lele)"
my_person.walk()


class MyOtherPerson:
    def __init__(self, name , surname):
        self.__name = name
        self.__surname = surname
        self.full_name = f"{name} {surname}"

    def walk(self):
        print(f"{self.full_name} está caminando")

    def get_name(self):
        return self.__name
    
    def get_surname(self):
        return self.__surname

my_other_person = MyOtherPerson("Jordi", "Ye")
print(my_other_person.get_name())

