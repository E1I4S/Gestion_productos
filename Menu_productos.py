productos = []

def cargar_datos():
    global productos
    try:
        with open("productos.txt", "r") as archivo:
            for linea in archivo:
                nombre, precio, cantidad = linea.strip().split(",")
                producto = {
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cantidad)
                }
                productos.append(producto)
        print("Datos cargados correctamente.")
    except FileNotFoundError:
        print("Archivo no encontrado. Iniciando con lista vacía.")
    except ValueError:
        print("El archivo contiene datos corruptos. Iniciando con lista vacía.")
        productos = []

def guardar_datos():
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
            archivo.write(linea)
    print("Datos guardados correctamente.")

def añadir_producto():
    nombre = input("Introduce el nombre del producto: ")
    while True:
        try:
            precio = float(input("Introduce el precio del producto: "))
            break
        except ValueError:
            print("Error: Debes introducir un número válido para el precio.")

    while True:
        try:
            cantidad = int(input("Introduce la cantidad disponible del producto: "))
            break
        except ValueError:
            print("Error: Debes introducir un número válido para la cantidad.")

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    productos.append(producto)
    print(f"Producto '{nombre}' añadido correctamente.")

def ver_productos():
    if productos:
        for idx, producto in enumerate(productos, 1):
            print(f"{idx}. {producto['nombre']} - Precio: {producto['precio']} - Cantidad: {producto['cantidad']}")
    else:
        print("No hay productos en la lista.")

def actualizar_producto():
    ver_productos()
    if productos:
        while True:
            try:
                indice = int(input("Introduce el número del producto a actualizar: "))
                if 1 <= indice <= len(productos):
                    producto = productos[indice - 1]
                    print(f"Actualizando el producto '{producto['nombre']}'.")

                    nuevo_nombre = input(f"Introduce el nuevo nombre (actual: {producto['nombre']}): ") or producto['nombre']

                    while True:
                        try:
                            nuevo_precio = input(f"Introduce el nuevo precio (actual: {producto['precio']}): ")
                            nuevo_precio = float(nuevo_precio) if nuevo_precio else producto['precio']
                            break
                        except ValueError:
                            print("Error: Debes introducir un número válido para el precio.")

                    while True:
                        try:
                            nueva_cantidad = input(f"Introduce la nueva cantidad (actual: {producto['cantidad']}): ")
                            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else producto['cantidad']
                            break
                        except ValueError:
                            print("Error: Debes introducir un número válido para la cantidad.")

                    productos[indice - 1] = {
                        "nombre": nuevo_nombre,
                        "precio": nuevo_precio,
                        "cantidad": nueva_cantidad
                    }
                    print(f"Producto '{nuevo_nombre}' actualizado correctamente.")
                    break
                else:
                    print("Error: Número de producto fuera de rango.")
            except ValueError:
                print("Error: Debes introducir un número válido.")

def eliminar_producto():
    ver_productos()
    if productos:
        while True:
            try:
                indice = int(input("Introduce el número del producto a eliminar: "))
                if 1 <= indice <= len(productos):
                    producto_eliminado = productos.pop(indice - 1)
                    print(f"Producto '{producto_eliminado['nombre']}' eliminado correctamente.")
                    break
                else:
                    print("Error: Número de producto fuera de rango.")
            except ValueError:
                print("Error: Debes introducir un número válido.")

def menu():
    cargar_datos()

    while True:
        print("\n--- Menú ---")
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")

menu()
