class Cuenta:
    def __init__(self, iban: str, saldo_actual: float, gasto_total_ultimo_mes: float, ingreso_total_ultimo_mes: float):
        pass # Implementar
        self.iban= iban
        self.saldo_actual= saldo_actual
        self.gasto_total_ultimo_mes= gasto_total_ultimo_mes
        self.ingreso_total_ultimo_mes= ingreso_total_ultimo_mes
    #un método que indique si el saldo de la cuenta es negativo
    def saldo_negativo(self):
      return self.saldo_actual <0




