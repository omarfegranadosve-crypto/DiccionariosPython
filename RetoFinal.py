def reg_ele():
    inventario = []
    print("Opción de Registro de los elementos de Laboratorio ECCI")
    print("")
    while True:
	print("")
        print("Ingrese los datos del nuevo elemento:")
        codigo = input("Código: ").strip()
        nombre = input("Nombre: ").strip()
        categoria = input("Categoría: ").strip()
        
        while True:
            try:
            cantidad = int(input("Cantidad: "))
            if cantidad >= 0:
                break
            else:
       	        print(" Error: La cantidad debe ser mayor o igual a cero.")
        
        estado = input("Estado por favor definalo como:(Disponible, En uso, Mantenimiento): ").strip()      
        elemento = {
            "codigo": codigo,
            "nombre": "nombre",
            "categoria": "categoria",
            "cantidad": cantidad,
            "estado": "estado"
        }
        inventario.append(elemento)
        print(f" Elemento '{nombre}' registrado con éxito.")
        
        continuar = input("¿Desea registrar otro elemento? (s/n): ").strip().lower()
        if continuar != 's':
            break
            
    return inventario


def most_reg(inventario):

    print("\Elementos Registrados")
    print("")
    if not inventario:
        print("El inventario está vacío.")
        return
        
    for idx, elem in enumerate(inventario, 1):
        print(f"{idx}. Código: {elem['codigo']} | Nombre: {elem['nombre']} | "
              f"Categoría: {elem['categoria']} | Cantidad: {elem['cantidad']} | Estado: {elem['estado']}")


def busccod(inventario):
    print("Busqueda de elementos")
    print("")
    codbus = input("Ingrese el código del elemento que desea buscar: ").strip()
    encontrado = False
    for elem in inventario:
        if elem['codigo'] == codbus:
            print(f" Elemento Encontrado:"
                  f" Nombre: {elem["nombre"]}\n"
                  f" Categoría: {elem["categoria"]}\n"
                  f" Cantidad: {elem["cantidad"]}\n"
                  f" Estado: {elem["estado"]}\n")
            encontrado = True
            break          
    if not encontrado:
        print(" No se encontró ningún elemento con ese código.")

def contdisp(inventario):
    print("Elementos Disponibles")
    print("")
    disponibles = sum(1 for elem in inventario if elem['estado'].strip().lower() == 'disponible')
    print(f" Total de elementos Disponibles: {disponibles}")


def mostmayorcant(inventario):
    print("MAyor cantidad de elementos")
    if not inventario:
        print("El inventario está vacío.")
        return
     
    elemmayor = max(inventario, key=lambda x: x['cantidad'])
    
    print(f"El elemento con más existencias es:\n"
          f"Nombre: {elemmayor['nombre']} (Código: {elemmayor['codigo']})\n"
          f"Cantidad: {elemmayor['cantidad']}")


def menu():
    inventario = []
    inventario = reg_ele()
    
    while True:
	print("")
        print("1. Mostrar todos los registros")
        print("2. Buscar un elemento por código")
        print("3. Contar cuántos elementos están disponibles")
        print("4. Mostrar el elemento con mayor cantidad")
        print("5. Registrar más elementos")
        print("6. Salir")
	print("")

        opcion = input("Seleccione una opción (1-6): ").strip()
        
        if opcion == '1':
            most_reg(inventario)
        elif opcion == '2':
            busccod(inventario)
        elif opcion == '3':
            contdisp(inventario)
        elif opcion == '4':
            mostmayorcant(inventario)
        elif opcion == '5':
            nuevos_elementos = reg_ele()
            inventario.extend(nuevos_elementos)
        elif opcion == '6':
            print("Gracias por usar el sistema de inventario ECCI")
            break
        else:
            print("Opción No válida. Escoger en el rango del 1 al 6.")

if __name__ == "__main__":
    menu()