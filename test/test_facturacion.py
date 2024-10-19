import unittest
from modelo.cliente import Cliente
from modelo.factura import Factura
from modelo.fertilizante import Fertilizante

class TestFacturacion(unittest.TestCase):

    def test_agregar_producto(self):
        cliente = Cliente("Juan Pérez", "12345678")
        factura = Factura(cliente, "2024-10-17")
        fertilizante = Fertilizante("Fertilizante A", 100000, "ICA123", "30 días", "2024-09-01")
        
        factura.agregar_producto(fertilizante)
        
        self.assertEqual(len(factura.productos), 1)
        self.assertEqual(factura.total, 100000)

if __name__ == '__main__':
    unittest.main()
