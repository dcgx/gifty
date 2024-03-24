global productos
productos = [{'Codigo':'01','Nombre':'Gifcard', 'Cantidad':5, 'Precio':5000, '' : ''},
            {'Codigo':'02','Nombre':'Flores', 'Cantidad':30, 'Precio':8000, '' : ''},
            {'Codigo':'03','Nombre':'Peluche', 'Cantidad':20, 'Precio':6000, '' : ''},
            {'Codigo':'04','Nombre':'Globos', 'Cantidad':5, 'Precio':4000, '' : ''},
            {'Codigo':'05','Nombre':'Tazones', 'Cantidad':30, 'Precio':3000, '' : ''}]

global registro_ventas
registro_ventas = {'Gifcard':0,'Flores':0,'Peluche':0,'Globos':0,'Tazones':0}

global productos_vendido
productos_vendido = []

global producto_a_buscar

def inventario():
    print("\n=== Inventario ===\n")
    for i in range(0,len(productos)):

        if productos[i].get('Cantidad') <= 5:
            print('\nProducto bajo stock 🛑\n')
            stock_producto = [productos[i]]
            for elem in stock_producto: #accedemos a cada elemento de la lista (en este caso cada elemento es un dictionario)
                for k,v in elem.items(): #acedemos a cada llave(k), valor(v) de cada diccionario
                    print(k, v)
        else:
            print('\nProducto con stock ✅\n')
            stock_producto = [productos[i]]
            for elem in stock_producto: #accedemos a cada elemento de la lista (en este caso cada elemento es un dictionario)
                for k,v in elem.items(): #acedemos a cada llave(k), valor(v) de cada diccionario
                    print(k, v)


    print('\nVolviendo...\n')


def ingresar_producto_a_buscar():
    nombre_codigo_prod = str(input("Ingrese el nombre o código del producto: "))
    producto_encontrado = buscar_producto(nombre_codigo_prod)
    print('\nProducto encontrado ✅\n')
    print('\n - Código: '+producto_encontrado.get('Codigo')+'\n - Nombre: '+producto_encontrado.get('Nombre')+'\n - Cantidad: '+str(producto_encontrado.get('Cantidad'))+'\n - Precio: '+str(producto_encontrado.get('Precio'))+'\n')

def buscar_producto(nombre_codigo_prod):
    print("\n=== Buscar Producto ===\n")
    producto_encontrado = None
    for i in range(0,len(productos)):
        print(productos[i].get('Codigo'))
        if productos[i].get('Nombre') == nombre_codigo_prod or productos[i].get('Codigo') == nombre_codigo_prod:
            producto_encontrado = productos[i]
    if producto_encontrado == None:
        print('\nProducto no encontrado ⚠️')
    return producto_encontrado

def stock():
    print("\n=== Stock Producto ===\n")
    for i in range(0,len(productos)-1):

        if productos[i].get('Cantidad') <= 5:
            stock_producto = [productos[i]]
            print('\nProducto bajo stock 🛑\n')
            for elem in stock_producto: #accedemos a cada elemento de la lista (en este caso cada elemento es un dictionario)
                for k,v in elem.items(): #acedemos a cada llave(k), valor(v) de cada diccionario
                    print(k, v)
    print('\nVolviendo...\n')

def ventas():
    print("\n=== Ventas ===\n")
    i=1
    if len(productos_vendido) >= 1:
        for elem in productos_vendido: #accedemos a cada elemento de la lista (en este caso cada elemento es un dictionario)
            mensaje = str(i)+'.-Venta'
            print(mensaje)
            for k,v in elem.items(): #acedemos a cada llave(k), valor(v) de cada diccionario
                    
                    print(k, v)
            i = i+1
    else:
        print('\nNo existen ventas\n')
    print('\nVolviendo...\n')