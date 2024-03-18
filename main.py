productos = []

def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
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
    generar_menu(opciones, '4')


def gestion_producto():
    print("=== Gestionar Productos ===")
    submenu = {
        '1': ('Agregar Producto', agregar_producto),
        '2': ('Modificar Producto', modificar_producto),
        '3': ('Eliminar Producto', eliminar_producto),
        '4': ('Volver atrás', lambda: print('Volviendo...'))
    }
    generar_menu(submenu, '4')

def agregar_producto():
    # Agregar producto
    nombre = input("Nombre del producto: ")
    precio = input("Precio del producto: ")
    cantidad = int(input("Cantidad del producto: "))
    num_disponible = int(input("Número de productos disponibles: "))
    productos.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "num_disponible": num_disponible
    })

def modificar_producto():
    nombre = input("Nombre del producto a modificar: ")
    for producto in productos:
        if producto["nombre"] == nombre:
            producto["nombre"] = input("Nuevo nombre del producto: ")
            producto["precio"] = input("Nuevo precio del producto: ")
            producto["cantidad"] = input("Nueva cantidad del producto: ")
            producto["num_disponible"] = input("Nuevo número de productos disponibles: ")
            break

def eliminar_producto():
    nombre = input("Nombre del producto a eliminar: ")
    for producto in productos:
        if producto["nombre"] == nombre:
            productos.remove(producto)
            print(f'Producto {nombre} eliminado correctamente.')
            break

def inventario():
    print('Has elegido la opción 2')

def buscar_producto():
    print('Has elegido la opción 3')

def stock():
    print('Has elegido la opción 4')

def reportes():
    total_productos = len(productos)
    productos_ordenados_por_categoria = sorted(productos, key=lambda x: x['cantidad'])
    producto_mas_vendido = productos_ordenados_por_categoria[0] if productos_ordenados_por_categoria else None
    productos_bajo_stock = []

    for producto in productos:
        if producto['num_disponible'] < 10:
            productos_bajo_stock.append(producto)
    print("======================== Reporte de Inventario ========================")
    print(f"Total de productos en inventario: {total_productos}")
    print("-------------------------------------------------------------------------")
    if producto_mas_vendido:
        print("Producto más vendido: ✅")
        print(f"  - Nombre: {producto_mas_vendido['nombre']}")
        print(f"  - Cantidad: {producto_mas_vendido['cantidad']}")
    else:
        print(f"Producto más vendido:")
        print(f"  - Nombre: No hay productos en inventario.")
        print(f"  - Cantidad: No hay productos en inventario.")
    print("-------------------------------------------------------------------------")
    print("Productos con bajo stock: ⚠️")
    if productos_bajo_stock:
        for producto in productos_bajo_stock:
            print(f"  - Nombre: {producto['nombre']}")
            print(f"  - Cantidad: {producto['cantidad']}")
    else:
        print(f"  - Nombre: No hay productos bajo stock.")
        print(f"  - Cantidad: No hay productos bajo stock.")
    print("=========================================================================")

def salir():
    print('Saliendo...')
    exit(0)

if __name__ == '__main__':
    menu_principal()

