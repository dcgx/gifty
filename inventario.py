from Gestion_producto import producto

def inventario():
    print("\n=== Inventario ===\n")
    for elem in producto: #accedemos a cada elemento de la lista (en este caso cada elemento es un dictionario)
        for k,v in elem.items(): #acedemos a cada llave(k), valor(v) de cada diccionario
            print(k, v)

def buscar_producto():
    print("\n=== Buscar Producto ===\n")
    dato_prod = str(input("Ingrese el nombre o código del producto: "))

    for i in range(0,len(producto)-1):

        if producto[i].get('Nombre:') == dato_prod or producto[i].get('Codigo:') == dato_prod:
            buscar_producto = [producto[i]]
            print('\nProducto encontrado ✅\n')
            for elem in buscar_producto: #accedemos a cada elemento de la lista (en este caso cada elemento es un dictionario)
                for k,v in elem.items(): #acedemos a cada llave(k), valor(v) de cada diccionario
                    print(k, v)
            break
    else:
        print('\nProducto no encontrado ⚠️')
    print('\nVolviendo...\n')

def stock():
    print("\n=== Stock Producto ===\n")
    for i in range(0,len(producto)-1):

        if producto[i].get('Cantidad:') <= 5:
            stock_producto = [producto[i]]
            print('\nProducto bajo stock 🛑\n')
            for elem in stock_producto: #accedemos a cada elemento de la lista (en este caso cada elemento es un dictionario)
                for k,v in elem.items(): #acedemos a cada llave(k), valor(v) de cada diccionario
                    print(k, v)


    print('\nVolviendo...\n')