# Enteros - integer
num1 = 5
num2 = -10
num3 = 0

# Flotante o float
a = 3.1416
b = 8.90
c = 90.35
d = -6.78
e = 0.00

# Cadenas o string
nombre = "Albiceleste"
direccion = 'Python es bacano!'

# Boleanos or boolean
is_raining = True
is_sunny = False

# Data Types - Lista o list
user_lst = ["Jeerson", "Marvin", "Dibbhier",
            "Beatriz", "Hector", "Alvison", "Jairo"]
combined_lst = [num1, "Maria Esther", a, direccion]
player_lst = ["Leo Messi", "Kylian Mbappe"]
amount_lst = [2, 3, 7, 8, 5, 5, 6, 1, 2, 3, 5, 3, 3, 4, 3, 2]
unsorted_lst = [3, 5, 4, 7, 6, 2, 1]
names_lst = ["Neymar Jr", "Vini Jr", "CR7", 8, True]

# Data Types - Listas con Funcion Built-in de Python
fruits_lst = list(["Apple", "Banana", "Orange"])
cities_lst = list(["Granada", "Leon"])

# Data Types - Tupla o tuple
phone_numbers_tpl = ("89067856", "34567890", "88638751", "90234567")
colors_tpl = ("red", "green", "yellow")
languages_tpl = ("Python", "Golang", "JavaScript", "Java")

# Data Types - Tuples declarados con funcion built-in de Python
grades_tpl = tuple([1, 2, 3, 4])
fruits_tpl = tuple(["Apple", "Banana", "Orange", "Mango", "Pear"])

# Data Types - Diccionarios o dictionary
simple_dict = {"language": "Python", "country": "Nicaragua"}

# Data Types - Diccionarios con Diccionarios como elementos
developers_dict = {"dev1": {"name": "Beatriz", "age": 23, "ciudad": "Managua"},
                   "dev2": {"name": "Marvin", "age": 47, "ciudad": "Rivas"},
                   "dev3": {"name": "Hector", "age": 27, "ciudad": "Cordoba"}
                   }

# suma simple de variables usando print para ver en pantalla
print(num1+a)

# Suma de elementos de lista
print(sum(amount_lst))

# Retornar ultimo elemento de lista
print(user_lst[-1])

# List Methods
print("Lista de Usuarios: ", user_lst)

# Append
user_lst.append("Juan")
print("Lista de Usuarios Modificada: ", user_lst)

# Elementos especificos de la lista
print(f"El segundo valor de esta lista es: {combined_lst[1:2]}")

# Conteo de elementos de lista usando len
print(f"La Lista {user_lst} tiene {len(user_lst)} elementos")

# Conteo de elementos repetidos en lista y diferentes formas de imprimir
print(f"El numero 3 se repite {amount_lst.count(3)} veces en esta lista")
print("El numero 2 se repite", amount_lst.count(2), " veces en esta lista")
print("El numero 5 se repite " + str(amount_lst.count(5)) + " veces en esta lista")

# Usando el metodo extend para juntar dos listas con elementos especificos
player_lst.extend(names_lst[:3])
print(player_lst)

# Ordenamiento de listas
print(f"Desordenada: {unsorted_lst}")

# Ordenar la lista
unsorted_lst.sort()
print(f"Ordenada: {unsorted_lst}")

# Revertir el orden de lista
unsorted_lst.sort(reverse=True)
print(f"Revertida: {unsorted_lst}")

# Ejemplos de metodos de listas
print(f"Inicial: {cities_lst}")

# usamos append para agregar otra ciudad
cities_lst.append("Managua")
print(f"Con mas Ciudades: {cities_lst}")

# usamos insert para agregar otra ciudad en posicion especifica
cities_lst.insert(2, "Jinotepe")
print(f"Actualizada con insert: {cities_lst}")

# encontramos posicion en lista de la ciudad a borrar
curr_position = cities_lst.index("Jinotepe")
print(f"Encontrar posicion de ciudad: {curr_position}")

# Borramos ciudad con la posicion de esta variable
cities_lst.pop(curr_position)
print(f"Borrada Ciudad de Jinotepe: {cities_lst}")

# usamoss remove para borrar el elemento pasado como parametro
cities_lst.remove("Leon")
print(f"Borrada Ciudad de Leon: {cities_lst}")

# Imprimir Tuples
print(f"Lenguaje Favorito: {languages_tpl[0]}")
print(f"Numero de Telefono: {phone_numbers_tpl[2]}")
print(f"Fruta Tropical abundante en Nicaragua: {fruits_tpl[3]}")

# Imprimir Diccionarios por referencia de llaves
print(f"Diccionario simple: {simple_dict['language']}")

# Imprimir el valor de dictionaries multiples por llaves
print(f"Diccionario Multiple llamado con llaves: {developers_dict['dev1']}")
