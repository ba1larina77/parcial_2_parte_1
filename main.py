from modelo.cliente import Cliente
from modelo.fertilizante import Fertilizante
from modelo.control_plagas import ControlPlagas
from modelo.antibiotico import Antibiotico
from modelo.factura import Factura

# Ejemplo de uso
cliente = Cliente("Juan Pérez", "12345678")
factura = Factura(cliente, "2024-10-17")

fertilizante = Fertilizante("Fertilizante A", 100000, "ICA123", "30 días", "2024-09-01")
control_plagas = ControlPlagas("Control de Plagas B", 150000, "ICA456", "15 días", 7)
antibiotico = Antibiotico("Antibiótico C", 80000, 500, "Bovinos")

factura.agregar_producto(fertilizante)
factura.agregar_producto(control_plagas)
factura.agregar_producto(antibiotico)

factura.mostrar_factura()
