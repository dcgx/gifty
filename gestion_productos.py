global producto

producto = [{'Codigo:':'01','Nombre:':'Gifcard', 'Cantidad:':5, 'Precio:':5000, '' : ''},
            {'Codigo:':'02','Nombre:':'Flores', 'Cantidad:':30, 'Precio:':8000, '' : ''},
            {'Codigo:':'03','Nombre:':'Peluche', 'Cantidad:':20, 'Precio:':6000, '' : ''},
            {'Codigo:':'04','Nombre:':'Globos', 'Cantidad:':5, 'Precio:':4000, '' : ''},
            {'Codigo:':'05','Nombre:':'Tazones', 'Cantidad:':30, 'Precio:':3000, '' : ''}]

def agregar_producto():
    print("\n=== Agregar Producto ===\n")
    codigo = str(input("Ingrese el código del producto: "))
    nombre = str(input("Ingrese el nombre del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    precio = int(input("Ingrese el precio del producto: "))

    prod_nuevo = {'Codigo:':codigo,'Nombre:':nombre, 'Cantidad:':cantidad, 'Precio:':precio, '' : ''}

    producto.append(prod_nuevo)

    print('Nuevo producto agregado ✅\n')

def modificar_producto():
    print('Has elegido la opción 2')

def eliminar_producto():
    print("\n=== Eliminar Producto ===\n")
    nombre = str(input("Ingrese el nombre del producto: "))

    for i in range(0,len(producto)-1):

        if producto[i].get('Nombre:') == nombre:
            del producto[i]
            print('Producto eliminado ✅: '+nombre+'\n')
            break
    else:
        print('\nProducto no encontrado ⚠️')
    print('\nVolviendo...\n')

