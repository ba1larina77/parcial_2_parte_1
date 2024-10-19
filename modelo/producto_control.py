from .producto import Producto

class ProductoControl(Producto):
    def __init__(self, nombre, precio, registro_ICA, frecuencia_aplicacion):
        super().__init__(nombre, precio)
        self.registro_ICA = registro_ICA
        self.frecuencia_aplicacion = frecuencia_aplicacion
