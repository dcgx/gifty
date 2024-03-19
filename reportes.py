def reportes():
    total_productos = len(producto)
    productos_ordenados_por_categoria = sorted(producto, key=lambda x: x['cantidad'])
    producto_mas_vendido = productos_ordenados_por_categoria[0] if productos_ordenados_por_categoria else None
    productos_bajo_stock = []

    for producto in producto:
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
