class Factura:
    def __init__(self, cliente, fecha):
        self.cliente = cliente
        self.fecha = fecha
        self.productos = []
        self.total = 0

    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.total += producto.precio

    def mostrar_factura(self):
        print(f"Factura para {self.cliente.nombre} ({self.cliente.cedula})")
        print(f"Fecha: {self.fecha}")
        print("Productos comprados:")
        for producto in self.productos:
            print(f"- {producto.nombre}: ${producto.precio}")
        print(f"Total a pagar: ${self.total}")
