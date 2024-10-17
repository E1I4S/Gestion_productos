import json
import os

productos = []

def crear_producto(nombre, precio, cantidad):
    return {"nombre": nombre, "precio": precio, "cantidad": cantidad}

def añadir_producto():
    try:
        nombre = input("Introduce el nombre del producto: ")
        precio = float(input("Introduce el precio del producto: "))
        cantidad = int(input("Introduce la cantidad del producto: "))
        producto = crear_producto(nombre, precio, cantidad)
        productos.append(producto)
        print(f"Producto '{nombre}' añadido correctamente.")
    except ValueError:
        print("Error: Precio y cantidad deben ser valores numéricos.")

def ver_productos():
    if len(productos) == 0:
        print("No hay productos en la lista.")
    else:
        for idx, producto in enumerate(productos, 1):
            print(f"{idx}. {producto['nombre']} - Precio: ${producto['precio']} - Cantidad: {producto['cantidad']}")

def actualizar_producto():
    ver_productos()
    if len(productos) == 0:
        return

    try:
        indice = int(input("Selecciona el número del producto a actualizar: ")) - 1
        if 0 <= indice < len(productos):
            nombre = input(f"Introduce el nuevo nombre del producto (actual: {productos[indice]['nombre']}): ") or productos[indice]['nombre']
            precio = input(f"Introduce el nuevo precio (actual: {productos[indice]['precio']}): ")
            precio = float(precio) if precio else productos[indice]['precio']
            cantidad = input(f"Introduce la nueva cantidad (actual: {productos[indice]['cantidad']}): ")
            cantidad = int(cantidad) if cantidad else productos[indice]['cantidad']

            productos[indice] = crear_producto(nombre, precio, cantidad)
            print(f"Producto '{nombre}' actualizado correctamente.")
        else:
            print("Error: Número de producto inválido.")
    except ValueError:
        print("Error: Entrada no válida. Asegúrate de introducir un número para seleccionar el producto.")

def eliminar_producto():
    ver_productos()
    if len(productos) == 0:
        return

    try:
        indice = int(input("Selecciona el número del producto a eliminar: ")) - 1
        if 0 <= indice < len(productos):
            eliminado = productos.pop(indice)
            print(f"Producto '{eliminado['nombre']}' eliminado correctamente.")
        else:
            print("Error: Número de producto inválido.")
    except ValueError:
        print("Error: Entrada no válida. Asegúrate de introducir un número para seleccionar el producto.")

def guardar_datos():
    try:
        with open("productos.txt", "w") as archivo:
            json.dump(productos, archivo)
        print("Datos guardados correctamente en 'productos.txt'.")
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

def cargar_datos():
    if os.path.exists("productos.txt"):
        try:
            with open("productos.txt", "r") as archivo:
                global productos
                productos = json.load(archivo)
            print("Datos cargados correctamente desde 'productos.txt'.")
        except Exception as e:
            print(f"Error al cargar los datos: {e}")
    else:
        print("No se encontró el archivo 'productos.txt'. Se iniciará con una lista vacía.")

def menu():
    cargar_datos() 
    while True:
        print("\n--- Menú ---")
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ").strip()

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
            print("Saliendo del programa...")
            break
        else:
            print("Por favor, selecciona una opción válida (1-5).")

if __name__ == "__main__":
    menu()
