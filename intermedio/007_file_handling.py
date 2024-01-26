### File Handling   ###

# .txt file
#txt_file = open("intermedio/my_file.txt", "w") # Solo escribe
#txt_file = open("intermedio/my_file.txt", "r") # Solo lee
#txt_file = open("intermedio/my_file.txt", "w+")    # Sobreescribir
import os


txt_file = open("intermedio/py_file.txt", "r+") # Leer y escribir
print(txt_file.read(5))
print(txt_file.read())

txt_file = open("intermedio/py_file.txt", "r+")
print(txt_file.read())
print(txt_file.read(5))

txt_file = open("intermedio/py_file.txt", "r+")
for line in txt_file.readlines():
    print(line)

txt_file.write("\nTesting .txt file")

#Crea, escribe, cierra y elimina
txt_file = open("intermedio/testing_file.txt", "w+")
txt_file.write("Jialiang\n Ye\n Yan\n 27 Años\n Estoy aprendiendo a programar en Python\n")
txt_file.close()
os.remove("intermedio/testing_file.txt")


# .json file
import json

json_file = open("intermedio/json_file.json", "w+")

json_test = {
    "name": "Jordi",
    "surname": "Ye",
    "age": 27,
    "language": ["Python", "Java", "Kotlin", "JavaScript"],
    "website": "https://www.google.es"
}

json.dump(json_test, json_file, indent = 2)
json_file.close()

with open("intermedio/json_file.json") as my_json_file:
    for line in my_json_file.readlines():
        print(line)

dict_json = json.load(open("intermedio/json_file.json"))
print(dict_json)
print(type(dict_json))
print(dict_json["name"])


# .csv file
import csv

csv_file = open("intermedio/csv_file.csv", "w+")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["Jordi", "Ye", 27, "Python", "www.google.es"])
csv_writer.writerow(["Jialiang", "", 0, "Java", "www.w3school.es"])
csv_file.close()

with open("intermedio/csv_file.csv") as my_json_file:
    for line in my_json_file.readlines():
        print(line)

# .xlsx file
import xlrd

"""
No se ha hecho pruebas para .xlsx an
"""


# .xml file
import xml

"""
No se ha hecho pruebas para .xlsx an
"""

