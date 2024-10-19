from .producto_control import ProductoControl

class Fertilizante(ProductoControl):
    def __init__(self, nombre, precio, registro_ICA, frecuencia_aplicacion, fecha_ultima_aplicacion):
        super().__init__(nombre, precio, registro_ICA, frecuencia_aplicacion)
        self.fecha_ultima_aplicacion = fecha_ultima_aplicacion
