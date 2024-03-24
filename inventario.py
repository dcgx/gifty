from gestion_productos import productos

def inventario():
    print("\n=== Inventario ===\n")
    for elem in productos: #accedemos a cada elemento de la lista (en este caso cada elemento es un dictionario)
        for k,v in elem.items(): #acedemos a cada llave(k), valor(v) de cada diccionario
            print(k, v)

def buscar_producto():
    print("\n=== Buscar Producto ===\n")
    dato_prod = str(input("Ingrese el nombre o código del producto: "))

    for i in range(0,len(productos)):
        if productos[i].get('Nombre') == dato_prod or productos[i].get('Codigo') == dato_prod:
            buscar_producto = [productos[i]]
            print('\nProducto encontrado ✅\n')
            for elem in buscar_producto: 
                for k,v in elem.items(): 
                    print(k, v)
            break
    else:
        print('\nProducto no encontrado ⚠️')
    print('\nVolviendo...\n')

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