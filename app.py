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

def stock_categoria(categoria,productos,inventario):
    pass


def buscar_precio(precio_min, precio_max, productos, inventario):
    pass

def buscar_codigo(codigo, productos):
    pass

def agregar_producto(codigo, nombre, categoria, precio, disponible, stock, vendidos, productos,inventario):
    pass


def eliminar_producto(codigo, productos, inventario):
    pass

def mostrar_productos(productos, inventario):
    pass


def main():
    productos = {}
    inventario = {}

    mostrar_menu()
    leer_opcion()

