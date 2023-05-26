class Producto:
    def __init__(self, nombre, cantidad, cantidad_minima, precio_base, tipo=None):
        self.nombre = nombre
        self.cantidad = cantidad
        self.cantidad_minima = cantidad_minima
        self.precio_base = precio_base
        self.tipo = tipo
        self.cantidad_inicial = cantidad  # Added the attribute cantidad_inicial

    def calcular_precio_final(self):
        impuestos = {'papeleria': 0.16, 'supermercado': 0.04, 'drogueria': 0.12}
        impuesto = impuestos.get(self.tipo, 0)
        return self.precio_base * (1 + impuesto)


class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        nombres_productos = [p.nombre for p in self.productos]
        if producto.nombre in nombres_productos:
            print("******")
            print('Ya existe un producto con ese nombre.')
            print("******")
        else:
            self.productos.append(producto)
            print("##################################")
            print('Producto agregado correctamente.')
            print("******")

    def visualizar_productos(self):
        for producto in self.productos:
            print('Nombre:', producto.nombre)
            print('Tipo:', producto.tipo)
            print('Cantidad:', producto.cantidad)
            print('Cantidad mínima:', producto.cantidad_minima)
            print('Precio base:', producto.precio_base)
            print('Precio final:', producto.calcular_precio_final())
            print('-----------------------')

    def vender_producto(self, nombre, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre:
                if producto.cantidad >= cantidad:
                    producto.cantidad -= cantidad
                    print("******")
                    print('Venta realizada correctamente.')
                    print("******")
                else:
                    print("******")
                    print('No hay suficiente cantidad para vender.')
                    print("******")
                return
        print("******")
        print('No se encontró un producto con ese nombre.')
        print("******")

    def abastecer_producto(self, nombre, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre:
                producto.cantidad += cantidad
                print("******")
                print('Producto abastecido correctamente.')
                print("******")
                return
        print("******")
        print('No se encontró un producto con ese nombre.')
        print("******")

    def cambiar_producto(self, nombre, tipo, cantidad_minima, precio_base):
        for producto in self.productos:
            if producto.nombre == nombre:
                producto.tipo = tipo
                producto.cantidad_minima = cantidad_minima
                producto.precio_base = precio_base
                print("******")
                print('Producto modificado correctamente.')
                print("******")
                return
        print("******")
        print('No se encontró un producto con ese nombre.')
        print("******")

    def calcular_estadisticas_ventas(self):
        total_dinero_ventas = 0
        producto_mas_vendido = None
        producto_menos_vendido = None
        cantidad_max_vendida = 0
        cantidad_min_vendida = float('inf')

        for producto in self.productos:
            total_dinero_ventas += producto.calcular_precio_final() * (
                    producto.cantidad_inicial - producto.cantidad
            )

            cantidad_vendida = producto.cantidad_inicial - producto.cantidad
            if cantidad_vendida > cantidad_max_vendida:
                cantidad_max_vendida = cantidad_vendida
                producto_mas_vendido = producto.nombre

            if cantidad_vendida < cantidad_min_vendida:
                cantidad_min_vendida = cantidad_vendida
                producto_menos_vendido = producto.nombre

        if producto_mas_vendido:
            print("******")
            print('Producto más vendido:', producto_mas_vendido)
            print("******")
        else:
            print("******")
            print('No se han realizado ventas.')
            print("******")
        if producto_menos_vendido:
            print("******")
            print('Producto menos vendido:', producto_menos_vendido)
            print("******")
        else:
            print("******")
            print('No se han realizado ventas.')
            print("******")
        print("******")
        print('Dinero total obtenido por ventas:', total_dinero_ventas)
        print("******")
        print("******")
        print('Dinero promedio obtenido por unidad de producto vendida:',
              total_dinero_ventas / sum([producto.cantidad_inicial - producto.cantidad for producto in self.productos]))
        print("******")


tienda = Tienda()
print("******")
while True:
    print("* 1. Agregar producto                              *")
    print("*******")
    print("* 2. Visualizar productos                          *")
    print("*******")
    print("* 3. Vender producto                               *")
    print("*******")
    print("* 4. Abastecer producto                            *")
    print("*******")
    print("* 5. Cambiar producto                              *")
    print("*******")
    print("* 6. Calcular estadísticas de ventas               *")
    print("*******")
    print("* 7. Salir                                         *")
    print("*******")
    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        nombre = input("Ingrese el nombre del producto: ")
        tipo = input("Ingrese el tipo del producto (papeleria/supermercado/drogueria): ")
        cantidad = float(input("Ingrese la cantidad del producto: "))  # Convertir a float
        precio_base = float(input("Ingrese el precio base del producto: "))

        producto = Producto(nombre, cantidad, cantidad, precio_base, tipo)
        tienda.agregar_producto(producto)
    elif opcion == 2:
        tienda.visualizar_productos()
    elif opcion == 3:
        nombre = input("Ingrese el nombre del producto a vender: ")
        cantidad = int(input("Ingrese la cantidad a vender: "))
        tienda.vender_producto(nombre, cantidad)
    elif opcion == 4:
        nombre = input("Ingrese el nombre del producto a abastecer: ")
        cantidad = int(input("Ingrese la cantidad a abastecer: "))
        tienda.abastecer_producto(nombre, cantidad)
    elif opcion == 5:
        nombre = input("Ingrese el nombre del producto a cambiar: ")
        tipo = input("Ingrese el nuevo tipo del producto: ")
        cantidad_minima = int(input("Ingrese la nueva cantidad mínima del producto: "))
        precio_base = float(input("Ingrese el nuevo precio base del producto: "))
        tienda.cambiar_producto(nombre, tipo, cantidad_minima, precio_base)
    elif opcion == 6:
        tienda.calcular_estadisticas_ventas()
    elif opcion == 7:
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
