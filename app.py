import os
os.system("cls")

#Una pequeña empresa necesita desarrollar un sistema para administrar el registro de sus productos y controlar la
#disponibilidad de cada uno de ellos.
#El sistema deberá ser implementado en Python utilizando programación modular.
#Todo el comportamiento del sistema debe organizarse mediante funciones, validaciones de datos y un menú interactivo.



def mostrar_menu():
    print(""" ========== MENÚ PRINCIPAL ==========
    1. Stock por categoría
    2. Buscar productos por rango de precio
    3. Actualizar precio
    4. Agregar producto
    5. Eliminar producto
    6. Mostrar productos
    7. Salir
    ===================================""")


def leer_opcion():
    while True:
        try:
            opcion = int(input("Selecciona opcion."))
            if opcion >=1 and opcion <=7:
                return opcion
            else:
                print("Ingresa un numero dentro del rango")
        except ValueError:
            print("Ingresa una opcion valida")


def validar_codigo(codigo):
    return codigo.strip() != ""

def validar_nombre(nombre):
    return nombre.strip() != ""


def validar_categoria(categoria):
    return categoria.strip() != ""


def validar_precio(precio):
    return precio >0


def validar_disponible(disponible):
    if disponible == "s":
        return True
    elif disponible == "n":
        return False
    else:
        return False
    
def validar_stock(stock):
    return stock >=0


def validar_vendidos(vendidos):
    return vendidos >=0

def stock_categoria(categoria_buscada, productos, inventario):
    categoria_buscada = categoria_buscada.strip().upper()
    stock_total = 0
    for codigo, atributos in productos.items():
        if atributos[1].upper().strip() == categoria_buscada:
            stock_total += inventario[codigo][0] 
    print(f"Stock total para la categoría '{categoria_buscada}': {stock_total}")


def buscar_precio(precio_min, precio_max, productos, inventario):
    items = []
    if precio_max < precio_min:
        return False
    for codigo in productos:
        if (precio_min <= productos[codigo][2] <= precio_max) and inventario[codigo][0] > 0:
            item = [productos[codigo][1],productos[codigo][2]]
            items.append(item)
    return items

def ejecutar_buscar_precio(productos, inventario):
    while True:
        try:
            precio_min = int(input("Ingresa el precio mínimo: "))
            precio_max = int(input("Ingresa el precio máximo: "))
            if precio_min > precio_max:
                print("El precio mínimo no puede ser mayor al máximo. Intenta de nuevo.")
                continue
            break 
        except ValueError:
            print("Error: Debes ingresar números enteros.")
            
    buscar_precio(precio_min, precio_max, productos, inventario)

def buscar_precio(precio_min, precio_max, productos, inventario):
    productos_filtrados = []
    
    for codigo, datos in productos.items():
        precio = datos[2]
        stock = inventario[codigo][0]
        
        if precio_min <= precio <= precio_max and stock > 0:
            productos_filtrados.append((datos[0], codigo))
            
    if productos_filtrados:
        print("Producto encontrado")
        for nombre, codigo in productos_filtrados:
            print(f"{nombre}--{codigo}")
    else:
        print("No se encontro.")

def buscar_codigo(codigo, productos):
    codigo = codigo.upper().strip()
    if codigo in productos:
        return True
    
    return False
    

def actualizar_precio(codigo,nuevo_precio,productos):
    codigo = codigo.upper().strip()
    if buscar_codigo(codigo,productos):
        productos[codigo][2] = nuevo_precio
        return True
    return False



def agregar_producto_exe(productos, inventario):
    while True:
        codigo = input("Ingresa el código del producto: ")
        if not validar_codigo(codigo):
            print("Error: El código no puede estar vacío.")
            continue
        codigo = codigo.upper().strip()
        if buscar_codigo(codigo, productos):
            print("Error: Este código ya existe.")
            continue
        break 

    while True:
        nombre = input("Ingresa el nombre del producto: ")
        if validar_nombre(nombre):
            nombre = nombre.strip()
            break
        print("Error: El nombre no puede estar vacío.")

    while True:
        categoria = input("Ingresa la categoría: ")
        if validar_categoria(categoria):
            categoria = categoria.strip()
            break
        print("Error: La categoría no puede estar vacía.")

    while True:
        try:
            precio = int(input("Ingresa el precio del producto: "))
            if validar_precio(precio):
                break
            print("Error: El precio debe ser mayor que cero.")
        except ValueError:
            print("Error: Debes ingresar un número entero válido.")

    while True:
        disp_input = input("¿Está disponible? (s/n): ").lower().strip()
        if disp_input == "s":
            disponible = True
            break
        elif disp_input == "n":
            disponible = False
            break
        else:
            print("Error. Ingresa una respuesta valida")

    while True:
        try:
            stock = int(input("Ingresa el stock: "))
            if validar_stock(stock):
                break
            print("Error: El stock debe ser mayor o igual a cero.")
        except ValueError:
            print("Error: Debes ingresar un entero válido.")

    while True:
        try:
            vendidos = int(input("Ingresa la cantidad de vendidos: "))
            if validar_vendidos(vendidos):
                break
            print("Error: La cantidad debe ser mayor o igual a cero.")
        except ValueError:
            print("Error:Ingresa un número entero.")

    if agregar_producto(codigo, nombre, categoria, precio, disponible, stock, vendidos, productos, inventario):
        print(f"Producto {codigo} agregado exitosamente.")
    else:
        print("Hubo un error al guardar el producto.")

def agregar_producto(codigo, nombre, categoria, precio, disponible, stock, vendidos, productos, inventario):
    if buscar_codigo(codigo, productos):
        return False
    productos[codigo] = [nombre, categoria, precio, disponible]
    inventario[codigo] = [stock, vendidos]
    return True

def eliminar_producto(codigo, productos, inventario):
    codigo = codigo.upper().strip()
    if buscar_codigo(codigo, productos):
        del productos[codigo]
        del inventario[codigo]
        return True
    return False


def mostrar_productos(productos, inventario):
    
    if not productos:
        print("No hay productos registrados en el sistema.")
        return

    for codigo in productos:
        nombre = productos[codigo][0]
        categoria = productos[codigo][1]
        precio = productos[codigo][2]
        disponible = productos[codigo][3]
        
        stock = inventario[codigo][0]
        vendidos = inventario[codigo][1]
        
        print(f"\nCODIGO: {codigo}")
        print(f"Nombre: {nombre}")
        print(f"Categoria: {categoria}")
        print(f"Precio: {precio}")
        print(f"Disponible: {disponible}")
        print(f"Stock: {stock}")
        print(f"Vendidos: {vendidos}")
    print("============================")

def main():
    productos = {}
    inventario = {}

    while True:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            categoria = input("\nIngresa la categoría a buscar: ")
            stock_categoria(categoria, productos, inventario)
            
        elif opcion == 2:
            ejecutar_buscar_precio(productos, inventario)
            
        elif opcion == 3:
            while True:
                codigo = input("\nIngresa el código del producto a actualizar: ")
                try:
                    nuevo_precio = int(input("Ingresa el nuevo precio: "))
                    if actualizar_precio(codigo, nuevo_precio, productos):
                        print("Precio actualizado correctamente.")
                    else:
                        print("Código inexistente.")
                except ValueError:
                    print("Error: El precio debe ser un número entero.")
                
                continuar = input("¿Deseas actualizar otro precio? (s/n): ").strip().lower()
                if continuar != 's':
                    break
                    
        elif opcion == 4:
            agregar_producto_exe(productos, inventario)
            
        elif opcion == 5:
            codigo = input("Ingresa el código del producto a eliminar: ")
            if eliminar_producto(codigo, productos, inventario):
                print("Producto eliminado exitosamente.")
            else:
                print("No se pudo eliminar.")
                
        elif opcion == 6:
            mostrar_productos(productos, inventario)
            
        elif opcion == 7:
            print(" Saliendo del programa")
            break

main()