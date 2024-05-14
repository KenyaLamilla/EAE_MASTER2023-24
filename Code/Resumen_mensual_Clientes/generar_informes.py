from entidades.cliente import Cliente
from entidades.cuenta import Cuenta


def estado_clientes(clientes):
    informes = []
    for cliente in clientes:
        informes.append({
            'nombre_completo': cliente.nombre_completo(),
            'num_cuentas': len(cliente.cuentas),
            'saldo_total': cliente.saldo_total()
        })
    return informes

def clientes_mayor_edad_ingreso_total(clientes):
    informes = []
    for cliente in clientes:
        if cliente.es_mayor_de_edad():
            informes.append({
                'nombre_completo': cliente.nombre_completo(),
                'ingreso_total_ultimo_mes': cliente.ingreso_total_ultimo_mes()
            })
    return informes

def clientes_cuenta_sin_ingreso_ultimo_mes(clientes):
    informes = []
    for cliente in clientes:
        for cuenta in cliente.cuentas:
            if cuenta.ingreso_total_ultimo_mes == 0:
                informes.append({
                    'nombre_completo': cliente.nombre_completo(),
                    'iban': cuenta.iban
                })
                break
    return informes

def clientes_cuenta_saldo_negativo(clientes):
    informes = []
    for cliente in clientes:
        for cuenta in cliente.cuentas:
            if cuenta.saldo_negativo():
                informes.append({
                    'nombre_completo': cliente.nombre_completo(),
                    'iban': cuenta.iban
                })
                break
    return informes

def clientes_gasto_superior_al_33(clientes):
    informes = []
    for cliente in clientes:
        for cuenta in cliente.cuentas:
            if cuenta.gasto_total_ultimo_mes > 0.33 * cuenta.ingreso_total_ultimo_mes:
                informes.append({
                    'nombre_completo': cliente.nombre_completo(),
                    'gasto_total': cuenta.gasto_total_ultimo_mes,
                    'ingreso_total_ultimo_mes': cuenta.ingreso_total_ultimo_mes
                })
                break
    return informes

def top3_clientes_mayor_gasto(clientes):
    informes = []
    clientes.sort(key=lambda c: sum(cuenta.gasto_total_ultimo_mes for cuenta in c.cuentas), reverse=True)
    for cliente in clientes[:3]:
        informes.append({
            'nombre_completo': cliente.nombre_completo(),
            'gasto_total': sum(cuenta.gasto_total_ultimo_mes for cuenta in cliente.cuentas)
        })
    return informes




