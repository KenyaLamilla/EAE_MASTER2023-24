from typing import List

from entidades.cuenta import Cuenta

class Cliente:
    def __init__(self, id_cliente: str, nombre: str, apellidos: str, edad: int, cuentas: List[Cuenta]):
        pass # Implementar
        self.id_cliente= id_cliente
        self.nombre= nombre
        self.apellidos= apellidos
        self.edad= edad
        self.cuentas= cuentas
    def saldo_total(self):
        return sum(cuenta.saldo_actual for cuenta in self.cuentas)

    def ingreso_total_ultimo_mes(self):
        return sum(cuenta.ingreso_total_ultimo_mes for cuenta in self.cuentas)

    def gasto_total_ultimo_mes(self):
        return sum(cuenta.gasto_total_ultimo_mes for cuenta in self.cuentas)

    def nombre_completo(self):
        return f"{self.nombre} {self.apellidos}"

    def es_mayor_de_edad(self):
        return self.edad >= 18

      
        
