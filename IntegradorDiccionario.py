estudiantes=[]
cantidad=int(input("Ingrese la cantidad de estudiantes: "))

for i in range(cantidad):
    estudiante={}
    estudiante["nombre"]=input("Nombre: ")
    estudiante["promedio"]=float(input("Promedio: "))
    estudiantes.append(estudiante)

for estudiante in estudiantes:
    print(estudiante)
#----------------------------------------------------Agregar  mejor promedio
 
mejor=estudiantes[0]
 
for estudiante in estudiantes:
     if estudiante["promedio"]>mejor["promedio"]:
         mejor=estudiante
         
print("Mejor estudiante es:", mejor["nombre"], "con el promedio es:", mejor["promedio"])