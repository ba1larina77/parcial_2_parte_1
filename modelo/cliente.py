class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.historial_pedidos = []

    def agregar_pedido(self, pedido):
        self.historial_pedidos.append(pedido)
