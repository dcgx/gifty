from gestion_producto import *
from inventario import *
from reportes import *

def mostrar_menu(opciones):
    print('Seleccione una opción:\n')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

def leer_opcion(opciones):
    while (a := input('\nOpción: ')) not in opciones:
        print('\nOpción incorrecta, vuelva a intentarlo.')
    return a

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()

def menu_principal():
    opciones = {
        '1': ('Gestión Productos', gestion_producto),
        '2': ('Inventario', inventario),
        '3': ('Buscar Producto', buscar_producto),
        '4': ('Stock', stock),
        '5': ('Reportes', reportes),
        '6': ('Salir', salir)
    }
    generar_menu(opciones, '6')

def gestion_producto():
    print("\n=== Gestionar Productos ===\n")
    submenu = {
        '1': ('Agregar Producto', agregar_producto),
        '2': ('Modificar Producto', modificar_producto),
        '3': ('Eliminar Producto', eliminar_producto),
        '4': ('Volver atrás', lambda: print('Volviendo...'))
    }
    generar_menu(submenu, '4')

def salir():
    print('Saliendo...')
    exit(0)

if __name__ == '__main__':
    menu_principal()
