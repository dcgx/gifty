global productos

productos = [{'Codigo':'01','Nombre':'Gifcard', 'Cantidad':5, 'Precio':5000, '' : ''},
            {'Codigo':'02','Nombre':'Flores', 'Cantidad':30, 'Precio':8000, '' : ''},
            {'Codigo':'03','Nombre':'Peluche', 'Cantidad':20, 'Precio':6000, '' : ''},
            {'Codigo':'04','Nombre':'Globos', 'Cantidad':5, 'Precio':4000, '' : ''},
            {'Codigo':'05','Nombre':'Tazones', 'Cantidad':30, 'Precio':3000, '' : ''}]

def agregar_producto():
    print("\n=== Agregar Producto ===\n")
    codigo = str(input("Ingrese el código del producto: "))
    nombre = str(input("Ingrese el nombre del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    precio = int(input("Ingrese el precio del producto: "))

    prod_nuevo = {'Codigo:':codigo,'Nombre':nombre, 'Cantidad':cantidad, 'Precio:':precio, '' : ''}

    productos.append(prod_nuevo)

    print('Nuevo producto agregado ✅\n')

def modificar_producto():
    print("\n=== Modificar Producto ===\n")
    nombre_codigo = str(input("Ingrese el nombre del producto o código: "))
    for i in range(0,len(productos)):
        if productos[i].get('Nombre') == nombre_codigo or productos[i].get('Codigo') == nombre_codigo:
            cantidad = int(input("Ingrese la nueva cantidad del producto: "))
            precio = int(input("Ingrese el nuevo precio del producto: "))
            productos[i]['Cantidad'] = cantidad
            productos[i]['Precio'] = precio
            print('Producto modificado ✅: '+nombre_codigo+'\n')
            break
        else:
            print('\nProducto no encontrado ⚠️')
    
    print("Producto modificado correctamente\n")


def eliminar_producto():
    print("\n=== Eliminar Producto ===\n")
    nombre = str(input("Ingrese el nombre del producto: "))
    for i in range(0,len(productos)):
        if productos[i].get('Nombre') == nombre:
            del productos[i]
            print('Producto eliminado ✅: '+nombre+'\n')
            break
    else:
        print('\nProducto no encontrado ⚠️')
    print('\nVolviendo...\n')

