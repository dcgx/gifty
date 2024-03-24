from gestion_productos import agregar_producto, modificar_producto, eliminar_producto, vender_producto
from inventario import inventario, ingresar_producto_a_buscar, stock, ventas
from reportes import reportes

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
        '2': ('Stock', stock), 
        '3': ('Ventas', ventas),
        '4': ('Inventario', inventario),
        '5': ('Buscar Producto', ingresar_producto_a_buscar),
        '6': ('Reportes', reportes),
        '7': ('Salir', salir)
    }
    generar_menu(opciones, '6')

def gestion_producto():
    print("\n=== Gestionar Productos ===\n")
    submenu = {
        '1': ('Vender Producto', vender_producto),
        '2': ('Agregar Producto', agregar_producto),
        '3': ('Modificar Producto', modificar_producto),
        '4': ('Eliminar Producto', eliminar_producto),
        '5': ('Volver atrás', lambda: print('Volviendo...'))
    }
    generar_menu(submenu, '5')

def salir():
    print('Saliendo...')
    exit(0)

if __name__ == '__main__':
    menu_principal()
