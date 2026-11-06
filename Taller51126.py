
# PUNTO NO 1
# Cree un programa que solicite: nombre completo, edad, estatura y ciudad. El programa debe:
# a) Guardar los datos utilizando los tipos de datos apropiados.
# b) Mostrar el nombre en mayúsculas y la cantidad de caracteres que contiene sin contar espacios.
# c) Indicar mediante condicionales si la persona es menor de edad, adulta o adulta mayor.
# d) Indicar si la edad es par o impar.
# e) Mostrar una frase final utilizando f-string con todos los datos procesados.

nombre = input("Ingresa tu nombre completo: ")
edad = int(input("Ingresa tu edad: "))
estatura = float(input("Ingresa tu estatura (en metros): "))
ciudad = input("Ingresa tu ciudad: ")

print("")
print(f"El nombre en mayúsculas es: {nombre.upper()}")
print(f"La cantidad de caracteres (sin espacios): {len(nombre.replace(' ', ''))}")

if edad < 18:
    print("La persona es menor de edad.")
elif 18 <= edad < 60:
    print("La persona es adulto.")
else:
    print("La persona es adulto mayor.")

if edad % 2 == 0:
    print("La edad es par.")
else:
    print("La edad es impar.")
    
print(f"Los Datos son: {nombre.upper()} tiene {edad} años, mide {estatura} metros y vive en {ciudad}.")


# PUNTO NO 2
# Solicite al usuario cuántos números desea ingresar. 
# Luego almacenelos valores en una lista. Cree funciones para obtener:
# - suma y promedio;
# - número mayor y número menor;
# - cantidad de números pares e impares;
# - una nueva lista con los valores positivos;
# - un set con los valores únicos ingresados.
# Al finalizar, muestre un resumen completo. 
# El programa debe impedir que la cantidad inicial de números sea menor que 1.

while True:
    cant = int(input("Ingrese la cantidad de números que desea ingresar (mínimo 1): "))
    if cant >= 1:
        break
    print("Error: La cantidad debe ser al menos 1.")
num = []
for i in range(cant):
    nu = float(input(f"Ingrese el número {i+1}: "))
    num.append(nu)
    
def sumarf(numeros):
    return sum(numeros)
def promf(numeros): 
    return sum(numeros) / len(numeros)
def maxf(numeros):
    return max(numeros) 
def minf(numeros):
    return min(numeros)

print("")
print("La suma de los números es:", sumarf(num))
print("El promedio de los números es:", promf(num))
print("El número mayor es:", maxf(num))
print("El número menor es:", minf(num))

def contpares(numeros):
    cantnp = 0
    for n in numeros:
        if n % 2 == 0:
            cantnp += 1
    return cantnp

def contimpares(numeros):
    cantim = 0
    for n in numeros:
        if n % 2 != 0:
            cantim += 1
    return cantim
        
print("La cantidad de números pares es:", contpares(num))
print("La cantidad de números impares es:", contimpares(num))

numpos = []
for n in num:
    if n > 0:
        numpos.append(n)
print("")
print("La lista de números positivos es:", numpos)
print("El conjunto de valores únicos es:", set(num))
print("")
print("La información general del sistema es:")
print(f"Los números ingresados son: {num}, la suma es: {sumarf(num)}, el promedio es: {promf(num)}, el número mayor es: {maxf(num)}, el número menor es: {minf(num)}, la cantidad de números pares es: {contpares(num)}, la cantidad de números impares es: {contimpares(num)}, la lista de números positivos es: {numpos}, y el conjunto de valores únicos es: {set(num)}.")


# PUNTO NO 3
# Solicite una palabra o frase corta. 
# Cree una función recursiva que invierta el texto sin utilizar [::-1] ni la función reversed(). Después:
# a) muestre el texto original y el texto invertido;
# b) determine si el texto es un palíndromo ignorando mayúsculas y espacios;
# c) cuente cuántas vocales tiene utilizando un ciclo;
# d) guarde en una tupla el texto original, el invertido y la cantidad de vocales.

pal = input("\nIngrese una palabra o frase corta: ")

def invtext(text):
    if len(text) == 0:
        return text
    else:
        return text[-1] + invtext(text[:-1])
    
print("El texto original es:", pal, " y el texto invertido es:", invtext(pal))

def es_pal(text):
    limp = ""
    for caracter in text:
        if caracter != " ":
            limp += caracter.lower()
    return limp == invtext(limp)

print("")
if es_pal(pal):
    print(f"La palabra '{pal}' es un palíndromo.")
else:
    print(f"La palabra '{pal}' no es un palíndromo.")
    
def contvoc(text):
    vocales = "aeiouAEIOU"
    cont = 0
    for car in text:
        if car in vocales:
            cont += 1
    return cont

print("")
print(f"La cantidad de vocales en la palabra '{pal}' es: {contvoc(pal)}")
tuplapal = (pal, invtext(pal), contvoc(pal))
print(f"La información de la tupla es: {tuplapal}")

# PUNTO NO 4
# Cree una lista llamada estudiantes. 
# Cada elemento de la lista debe ser un diccionario con la estructura: {"nombre": ..., "codigo": ..., "notas": [...]}
# Registre tres estudiantes. Para cada uno solicite nombre, código y tres notas entre 0.0 y 5.0. El programa debe:
# a) validar que las notas se encuentren dentro del rango permitido;
# b) calcular el promedio mediante una función;
# c) agregar al diccionario las claves promedio y estado;
# d) asignar estado = "Aprobado" si el promedio es mayor o igual a 3.0; en caso contrario, "Reprobado";
# e) mostrar nombre, código, promedio y estado de cada estudiante.

estudiantes = []

def calcprom(notas):
    suma = 0
    for nota in notas:
        suma += nota
    return suma / len(notas)

def pednota(numero_nota):
    while True:
        nota = float(input(f"   Ingrese la nota {numero_nota} (0.0 - 5.0): "))
        if 0.0 <= nota <= 5.0:
            return nota
        else:
            print("Verifique la nota ingresada, debe estar entre 0.0 y 5.0. Intente de nuevo.")

def detestado(promedio):
    if promedio >= 3.0:
        return "Aprobado"
    else:
        return "Reprobado"

for i in range(3):
    print("")
    print(f"Ingrese los datos del Estudiante {i + 1}")
    nombre = input(" Ingrese el Nombre: ")
    codigo = input(" Ingrese el Código: ")

    notas = []
    for j in range(1, 4):
        nota = pednota(j)
        notas.append(nota)
    prom = calcprom(notas)
    estudiante = {
        "nombre": nombre,
        "codigo": codigo,
        "notas": notas,
        "promedio": prom,
        "estado": detestado(prom)
    }
    estudiantes.append(estudiante)

for estudiante in estudiantes:
    print(f"Nombre:   {estudiante['nombre']}")
    print(f"Código:   {estudiante['codigo']}")
    print(f"Notas:    {estudiante['notas']}")
    print(f"Promedio: {estudiante['promedio']}")
    print(f"Estado:   {estudiante['estado']}")

# PUNTO NO 5
# Se tienen los siguientes grupos de estudiantes:
# grupo_python = ["Ana", "Luis", "Carlos", "Sofia", "Mateo"]
# grupo_datos = ["Sofia", "Mateo", "Laura", "Ana", "Daniel"]
# Convierta las listas en sets y muestre:
# a) estudiantes que pertenecen a ambos grupos;
# b) estudiantes que solamente están en Python;
# c) estudiantes que solamente están en Datos;
# d) total de estudiantes diferentes;
# e) una lista ordenada alfabéticamente con todos los estudiantes sin repetir.
# Después cree un diccionario que tenga como clave el nombre del estudiante y como valor la cantidad de grupos a los que pertenece.

grupo_python = ["Ana", "Luis", "Carlos", "Sofia", "Mateo"]
grupo_datos = ["Sofia", "Mateo", "Laura", "Ana", "Daniel"]

setpython = set(grupo_python)
setdatos = set(grupo_datos)
print(f"Grupo Python en conjuntos es: {setpython}")
print(f"Grupo Datos en conjuntos es:  {setdatos}")

union = setpython & setdatos 
print(f"Los datos de los grupos unidos es:   {union}")

solopython = setpython - setdatos  
print(f"Aplicando la operación de Diferencia (quitando el conjunto de Datos) es:  {solopython}")

solodatos = setdatos - setpython  
print(f"Aplicando la operación de Diferencia (quitando el conjunto de Python) es:  {solodatos}")

dif = setpython | setdatos  
print(f"   {len(dif)} estudiantes -> {dif}")

listordenada = sorted(dif)
print("Lista ordenada alfabéticamente con todos los estudiantes sin repetir es:")
print(f"{listordenada}")

dicgrupos = {}

for estudiante in dif:
    cont = 0
    if estudiante in setpython:
        cont += 1
    if estudiante in setdatos:
        cont += 1
    dicgrupos[estudiante] = cont

for nombre, cantidad in dicgrupos.items():
    print(f"   {nombre} -> {cantidad} grupo(s)")

print("La información del Diccionario es:")
print(f"{dicgrupos}")

# PUNTO NO 6
# Desarrolle un pequeño sistema de inventario para una tienda. 
# El programa debe trabajar con una lista de diccionarios. Cada producto debe tener: codigo, nombre, precio, cantidad.
# Registre inicialmente tres productos y luego muestre un menú con estas opciones:
# 1. Mostrar inventario.
# 2. Buscar producto por código.
# 3. Calcular valor total del inventario.
# 4. Mostrar productos con cantidad menor que 5.
# 5. Salir.
# Requisitos obligatorios:
# - Utilizar un ciclo para mantener activo el menú hasta seleccionar Salir.
# - Crear al menos dos funciones para separar la lógica del programa.
# - Validar que precio y cantidad no sean negativos.
# - Utilizar strings para las búsquedas y mensajes mostrados al usuario.
# - Mostrar al final cuántos códigos de producto diferentes existen utilizando un set.

def mostinv(inv):
    if not inv:
        print("Actualmente el inventario está vacío.")
        return
    print(f"{'Código'} {'Nombre'} {'Precio'} {'Cantidad'}")
    print("")
    for prod in inv:
        print(f"{prod['codigo']} {prod['nombre']} ${prod['precio']} {prod['cantidad']}")

def buscprod(inv, codbus):
    for prod in inv:
        if prod["codigo"].lower() == codbus.lower():
            return prod
    return None

def calcvaltotal(inv):
    total = 0
    for prod in inv:
        total += prod["precio"] * prod["cantidad"]
    return total

def moststockbaj(inv, lim=5):
    encon = []
    for prod in inv:
        if prod["cantidad"] < lim:
            encon.append(prod)
    if not encon:
        print(f"\nActualmente no hay productos con stock menor a {lim}.")
        return
    print(f"\nProductos con stock menor a {lim}:")
    for prod in encon:
        print(f" - Código: {prod['codigo']} | Nombre: {prod['nombre']} (Cantidad: {prod['cantidad']})")

def pedirvalcorr(mens, es_entero=False):
    while True:

        if es_entero:
            valor = int(input(mens))
        else:
            valor = float(input(mens))
                
        if valor < 0:
            print("El valor no puede ser negativo. Ingrese nuevamente el valor.")
        else:
            return valor


def main():
    inventario = []
    print("Registro de los 3 productos iniciales")
    for i in range(1, 4):
        print(f"\nIngrese el Producto No {i}")
        codigo = input("Ingrese el Código: ").strip()
        nombre = input("Ingrese el Nombre: ").strip()
        precio = pedirvalcorr("Ingrese el Precio: ", es_entero=False)
        cantidad = pedirvalcorr("Ingrese la Cantidad: ", es_entero=True)
        
        producto = {
            "codigo": codigo,
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
        inventario.append(producto)

    while True:
        print("MENÚ DE INVENTARIO")
        print("")
        print("1. Mostrar inventario")
        print("2. Buscar producto por código")
        print("3. Calcular valor total del inventario")
        print("4. Mostrar productos con cantidad menor que 5")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ").strip()
        
        if opcion == "1":
            mostinv(inventario)
        elif opcion == "2":
            codbus = input("\nIngrese el código a buscar: ").strip()
            resultado = buscprod(inventario, codbus)
            if resultado:
                print("\n✓ Producto encontrado:")
                print(f" Código: {resultado['codigo']}")
                print(f" Nombre: {resultado['nombre']}")
                print(f" Precio: ${resultado['precio']}")
                print(f" Cantidad: {resultado['cantidad']}")
            else:
                print(f"No se encontró ningún producto con el código ingresado '{codbus}'.")
        elif opcion == "3":
            total = calcvaltotal(inventario)
            print(f"Valor total del inventario: ${total}")
        elif opcion == "4":
            moststockbaj(inventario, 5)
        elif opcion == "5":
            print("\nSaliendo del sistema...")
            break
        else:
            print("\n✗ Opción inválida. Ingrese un número entre 1 y 5.")

    coduni = set()
    for producto in inventario:
        coduni.add(producto["codigo"])
        
    print("Resultados Finales del Inventario")
    print("")
    print(f"La Cantidad de códigos diferentes de los productos es: {len(coduni)}")
    print(f"Los Códigos registrados son: {coduni}")

if __name__ == "__main__":
    main()
