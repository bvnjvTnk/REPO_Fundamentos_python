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
            if opcion >=1 and opcion <=6:
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
        print("Dato no valido")
        return
    
def validar_stock(stock):
    return stock >=0


def validar_vendidos(vendidos):
    return vendidos >=0

def stock_categoria(categoria,productos,inventario):
    categoria = categoria.strip().upper()
    total_encontrados=0
    for categoria, atributos in productos.items():
        if atributos[1].upper().strip() == categoria:
            total_encontrados = total_encontrados + 1
    return total_encontrados


def buscar_precio(precio_min, precio_max, productos, inventario):
    items = []
    if precio_max < precio_min:
        return False
    for codigo in productos:
        if (precio_min <= productos[codigo][2] <= precio_max) and inventario[codigo][0] > 0:
            item = [productos[codigo][1],productos[codigo][2]]
            items.append(item)
    return items

def buscar_codigo(codigo, inventario, productos):
    codigo = codigo.upper().strip()
    if codigo in productos and codigo in inventario:
        return True
    
    return False
    

def actualizar_precio(codigo,nuevo_precio,productos):
    codigo = codigo.upper().strip()
    if buscar_codigo(productos,codigo):
        productos[codigo][2] = nuevo_precio
        return True
    return False

def eliminar_producto(codigo, productos,inventario):
    codigo = codigo.upper().strip()
    if buscar_codigo(productos,codigo):
        del productos[codigo]
        del inventario[codigo]
        return True
    return False


def agregar_producto_exe(codigo, nombre, categoria, precio, disponible, stock, vendidos, productos,inventario):
    codigo = validar_codigo("Ingresa el codigo del producto: ")
    if not validar_codigo(productos,codigo):
        print("Error: Este codigo ya existe")
        return

    nombre = validar_nombre("Ingresa el nombre del producto: ")
    categoria = validar_categoria("Ingresa categoria: ")
    precio = validar_precio("Ingresa el precio del producto: ")
    disponible = validar_disponible("Ingrersa disponibilidad: ")
    stock = validar_stock("Ingresa stock: ")
    vendidos = 0
    agregar_producto(codigo,nombre,categoria,precio,disponible,stock,vendidos,productos,inventario)

def agregar_producto(codigo,nombre,categoria,precio,disponible,stock,vendidos,productos,inventario):
    if not validar_codigo(productos,codigo):
        return False
    productos[codigo] = [nombre,categoria,precio,disponible]
    inventario[codigo] = [stock,vendidos]
    return True


def eliminar_producto(codigo, productos, inventario):
    pass

def mostrar_productos(productos, inventario):
    pass

def main():
    productos = {
"P101":["Cuaderno","Papelería",2490,True],
"P102":["Lápiz","Papelería",590,True],
"P103":["Botella","Accesorios",6990,False],
"P104":["Mochila","Accesorios",24990,True]}
    inventario = {
    "P101":[30,15],
    "P102":[120,50],
    "P103":[0,10],
    "P104":[8,25]
    }

    mostrar_menu()
    leer_opcion()

