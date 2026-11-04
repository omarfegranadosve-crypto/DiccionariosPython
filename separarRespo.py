estudiante= {"nombre":"Ana", "promedio":4.4}

def mostrar_estudiante(estudiante):
    print("Nombre:", estudiante["nombre"])
    print("Promedio:", estudiante["promedio"])
    
def aprobo(estudiante):
    return estudiante["promedio"] >= 3.0

mostrar_estudiante(estudiante)
print("Aprobó:", aprobo(estudiante))

