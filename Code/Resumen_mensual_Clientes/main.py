
from entidades.cliente import Cliente
from entidades.cuenta import Cuenta
from generar_informes import ( 
    estado_clientes,
    clientes_mayor_edad_ingreso_total,
    clientes_cuenta_sin_ingreso_ultimo_mes,
    clientes_cuenta_saldo_negativo,
    clientes_gasto_superior_al_33,
    top3_clientes_mayor_gasto)


# Conjunto de datos
cuenta1 = Cuenta("0001", -5.25, 500.19, 0.0)
cuenta2 = Cuenta("0002", 10254.25, 222.45, 0.0)
cuenta3 = Cuenta("0003", 122.25, 20.25, 145.85)
cuenta4 = Cuenta("0004", 332.05, 251.04, 0.0)
cuenta5 = Cuenta("0005", 5454.19, 2251.04, 3510.44)
cuenta6 = Cuenta("0006", -164.01, 211.15, 200.0)
cuenta7 = Cuenta("0007", 15456.25, 1554.24, 2200.52)
cuenta8 = Cuenta("0008", 1245.47, 24.44, 500.0)
cuenta9 = Cuenta("0009", 15164.23, 0.0, 4200.92)
cuenta10 = Cuenta("0010", 4226.25, 25251.26, 0.0)
cuenta11 = Cuenta("0011", 14242.25, 656.74, 2520.14)
cuenta12 = Cuenta("0012", 2546.25, 1215.08, 1200.82)
cuenta13 = Cuenta("0013", 2425.26, 1250.04, 0.0)

cliente1 = Cliente("0001", "Juan", "Garcia", 38, [cuenta1, cuenta2])
cliente2 = Cliente("0002", "Laura", "Jimenez", 13, [cuenta3])
cliente3 = Cliente("0003", "Pedro", "Rodriguez", 17, [cuenta4])
cliente4 = Cliente("0004", "Andres", "Gomez", 56, [cuenta5, cuenta6])
cliente5 = Cliente("0005", "Gema", "Sanchez", 89, [cuenta7])
cliente6 = Cliente("0006", "Ana", "Jimenez", 16, [cuenta8])
cliente7 = Cliente("0007", "Jesus", "Perez", 55, [cuenta9, cuenta10])
cliente8 = Cliente("0008", "Jose", "Garcia", 26, [cuenta11])
cliente9 = Cliente("0009", "Angel", "Perez", 24, [cuenta12])
cliente10 = Cliente("0010", "Maria", "Gomez", 21, [cuenta13])

clientes = [cliente1, cliente2, cliente3, cliente4, cliente5, cliente6, cliente7, cliente8, cliente9, cliente10]

# Informe 1
informe1 = estado_clientes(clientes)
print("Informe 1: clientes con su número de cuentas y saldo total")
print("cliente,numero de cuentas,saldo total")
for informe in informe1:
    print(f"{informe['nombre_completo']},{informe['num_cuentas']},{informe['saldo_total']:.2f}")
print("\n10 filas\n")

# Informe 2
informe2 = clientes_mayor_edad_ingreso_total(clientes)
print("Informe 2: Ingreso de clientes mayor de edad")
print("cliente,ingreso ultimo mes")
for informe in informe2:
    print(f"{informe['nombre_completo']},{informe['ingreso_total_ultimo_mes']:.2f}")
print("\n7 filas\n")

# Informe 3
informe3 = clientes_cuenta_sin_ingreso_ultimo_mes(clientes)
print("Informe 3: Clientes con alguna cuenta sin ingreso")
print("cliente,iban")
for informe in informe3:
    print(f"{informe['nombre_completo']},{informe['iban']}")
print("\n5 filas\n")

# Informe 4
informe4 = clientes_cuenta_saldo_negativo(clientes)
print("Informe 4: Clientes con alguna cuenta con saldo negativo")
print("cliente,iban")
for informe in informe4:
    print(f"{informe['nombre_completo']},{informe['iban']}")
print("\n2 filas\n")

# Informe 5
informe5 = clientes_gasto_superior_al_33(clientes)
print("Informe 5: Clientes con gasto superior al 33% del ingreso en el último mes")
print("cliente,gasto total,ingreso total")
for informe in informe5:
    print(f"{informe['nombre_completo']},{informe['gasto_total']:.2f},{informe['ingreso_total_ultimo_mes']:.2f}")
print("\n7 filas\n")

# Informe 6
informe6 = top3_clientes_mayor_gasto(clientes)
print("Informe 6: Clientes top 3 con mayor gasto total")
print("cliente,gastos")
for informe in informe6:
    print(f"{informe['nombre_completo']},{informe['gasto_total']:.2f}")
print("\n3 filas\n")
