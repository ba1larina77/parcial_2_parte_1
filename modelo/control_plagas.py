from .producto_control import ProductoControl

class ControlPlagas(ProductoControl):
    def __init__(self, nombre, precio, registro_ICA, frecuencia_aplicacion, periodo_carencia):
        super().__init__(nombre, precio, registro_ICA, frecuencia_aplicacion)
        self.periodo_carencia = periodo_carencia
