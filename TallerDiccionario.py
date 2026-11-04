producto = {"codigo": "t123","nombre": "Televisor", "precio": 1500000,"stock": 10}
print("Informaciòn del Producto")
for pro in producto:
    print(f"{pro}: {producto[pro]}")
print("")

inventario = {
    "t123": {"nombre": "Televisor", "precio": 1500000, "stock": 10},
    "C201": {"nombre": "computador", "precio": 1250000, "stock": 10},
    "CL325": {"nombre": "Celular", "precio": 980000, "stock": 50},
    "TL432": {"nombre": "Tablet", "precio": 560000, "stock": 30}
}

print("Existencia de código en el inventario")
cod = input("Ingresa el código del producto a buscar (es alfanumerico): ")

if cod in inventario:
    print(f"El código '{cod}' SÍ existe en el inventario.")
    print("Detalles:", inventario[cod])
else:
    print(f"El código '{cod}' NO existe en el inventario.")
print()

materias = {"MatemáticasFiancieras": 4.2,"Programaciòn": 3.8,"Combinatoria": 4.5,"CàlculoDiferencial": 5.0,"Inglés": 4.0}
promMat = sum(materias.values()) / len(materias)

print("El Promedio de las materias es:")
print("Notas:", materias)
print(f"El promedio de las materias es: {promMat}")
print()

estudiantes = [
    {"nombre": "Otto", "promedio": 4.5},
    {"nombre": "Mary", "promedio": 3.8},
    {"nombre": "Julian", "promedio": 3.5},
    {"nombre": "Valentina", "promedio": 4.1},
    {"nombre": "Juan", "promedio": 2.0}
]

print("El promedio de los estudiantes >= 3.0")
print("")
for est in estudiantes:
    if est["promedio"] >= 3.0:
        print(f"Estudiante: {est['nombre']} | Promedio: {est['promedio']}")
print()

def calcvalInv(prod):
    precio = prod.get("precio", 0)
    stock = prod.get("stock", 0)
    return precio * stock

print("Valor total del inventario")
valtot= calcvalInv(producto)
print(f"El producto '{producto['nombre']}' tiene un valor total en inventario de: ${valtot}")
