from inventario import productos, productos_vendido, registro_ventas, buscar_producto

def agregar_producto():
    print("\n=== Agregar Producto ===\n")
    codigo = str(input("Ingrese el código del producto: "))
    nombre = str(input("Ingrese el nombre del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    precio = int(input("Ingrese el precio del producto: "))

    prod_nuevo = {'Codigo':codigo,'Nombre':nombre,'Cantidad':cantidad,'Precio':precio, '' : ''}
    productos.append(prod_nuevo)
    registro_ventas [nombre]= cantidad

    print('Nuevo producto agregado ✅\n')
    return productos

def modificar_producto():
    print("\n=== Modificar Producto ===\n")
    codigo = str(input("Ingrese el código del producto: "))
    nombre = str(input("Ingrese el nombre del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    precio = int(input("Ingrese el precio del producto: "))

    prod_nuevo = {'Codigo':codigo,'Nombre':nombre,'Cantidad':cantidad,'Precio':precio, '' : ''}

    for i in range(0,len(productos)):
        #Por cada posición de la lista, pregunta por el diccionario guardado y valida si nombre o código es igual a lo ingresado
        if productos[i].get('Codigo') == codigo:
            #Si encuentra el producto, guarda el resultado en una lista
            productos[i] = prod_nuevo
            print('\nProducto modificado ✅\n')
            break
    else:
        print('\nProducto no encontrado ⚠️')
    print('\nVolviendo...\n')
    return productos

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
    return productos

def vender_producto():
    print("\n=== Agregar Producto ===\n")
    producto_codigo = str(input("Ingrese el código del producto a vender: "))
    cantidad_vendida = int(input("Ingrese la cantidad del producto a vender: "))
    producto_encontrado = buscar_producto(producto_codigo)
    print(producto_encontrado)
    codigo = producto_encontrado.get('Codigo')
    nombre = producto_encontrado.get('Nombre')
    cantidad = producto_encontrado.get('Cantidad')
    precio = producto_encontrado.get('Precio')

    if cantidad >= cantidad_vendida:
        prod_vendido = {}
        nuevo_stock = {}
        monto_total = cantidad_vendida * precio
        prod_vendido = {'Codigo':producto_codigo,'Nombre':nombre,'Vendidas':cantidad_vendida,'Total':monto_total , '' : ''}
        nueva_cantidad = cantidad - cantidad_vendida
        nuevo_stock = {'Codigo':codigo,'Nombre':nombre,'Cantidad':nueva_cantidad,'Precio':precio, '' : ''}

        for i in range(0,len(productos)):
            #Por cada posición de la lista, pregunta por el diccionario guardado y valida si nombre o código es igual a lo ingresado
            if productos[i].get('Codigo') == codigo:
                #Si encuentra el producto, guarda el resultado en una lista
                productos[i] = nuevo_stock
                print('\nStock '+nombre+' modificado ✅\n')
                break
        print('Producto '+nombre+' Vendido ✅\n')
        productos_vendido.append(prod_vendido)

        if nombre in registro_ventas:
            cantidad = registro_ventas[nombre]
            nueva_cantidad = cantidad_vendida + cantidad
            registro_ventas[nombre] = nueva_cantidad
            return registro_ventas
        return productos
    else:
        print('\nNo hay stock ⚠️')
    
    print('\nVolviendo...\n')
    return productos