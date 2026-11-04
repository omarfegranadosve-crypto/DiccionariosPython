estudiante = {}

estudiante["nombre"] = input("Nombre: ")
estudiante["edad"] = int(input("Edad: "))
estudiante["programa"] = input("Programa: ")
estudiante["promedio"] = float(input("Promedio: "))
print("-"*20)
for clave, valor in estudiante.items():
    print(clave, ":", valor)