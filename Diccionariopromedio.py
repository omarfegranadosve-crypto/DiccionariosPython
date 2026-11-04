estudiante = {}

estudiante["nombre"] = input("Nombre: ")
estudiante["edad"] = int(input("Edad: "))
estudiante["programa"] = input("Programa: ")
estudiante["promedio"] = float(input("Promedio: "))
print("-"*20)
print("Validaciòn si el estudiante aprueba")

promedio= estudiante.get("promedio")
if promedio >= 3.0:
    estudiante["estado"] = "Aprobado"
else:
    estudiante["estado"] = "Reprobado"  
    
print(estudiante)