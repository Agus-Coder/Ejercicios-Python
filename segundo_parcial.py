"""

1) Se ingresa el nombre y apellido, el saldo de la caja de ahorro y el saldo de la caja de cuenta corriente de los clientes de un banco hasta que el nombre y apellido sea FIN. Calcular y mostrar:

    Nombre y apellido del cliente que tiene el mayor saldo en la caja de ahorro
    Cantidad de clientes cuyo saldo en caja de ahorro o en cuenta corriente sea negativo.
    Total de dinero depositado en ambas cajas.
    Mostrar el nombre y apellido de aquellos clientes que no tienen dinero en ambas cuentas.

"""

nombre_apellido = input("Ingrese su nombre y apellido. Ingrese FIN para finalizar el programa\n")

max_ca = 0
nombre_max_ca = ''
total_negativos = 0
total_ca = 0
total_cc = 0

while nombre_apellido != "FIN":
    saldo_ca = int(input("Ingrese saldo en su caja de ahorro \n"))
    saldo_cc = int(input("Ingrese saldo en su cuenta corriente \n"))

    if saldo_ca > max_ca:
        nombre_max_ca = nombre_apellido
    
    if saldo_ca < 0 or saldo_cc <0:
        total_negativos += 1
    
    if saldo_cc == 0 and saldo_ca ==0:
        print(nombre_apellido + " No posee saldo en ninguna de ambas cuentas\n")

    total_ca += saldo_ca
    total_cc += saldo_cc

    nombre_apellido = input("Ingrese su nombre y apellido \n")

print("El cliente que tiene el mayor saldo en la caja de ahorro es: " + nombre_max_ca + "\n")
print(f"Hay {total_negativos} con saldo negativo en al menos una de las cuentas")
print(f"Hay {total_ca} pesos en total depositados en las cajas de ahorro y {total_cc} depositados en las cuentas corrientes")


cadena = input("Ingrese algo con mas de 5 caracteres ")
cadena2 = input("Ingrese algo con mas de 5 caracteres ")

len1 = len(cadena)
len2 = len(cadena2)
cadena_modif = ''
cadena2_modif = ''
if len1 > len2:
    cadena_modif = "&&" + cadena

    for x in range(-1, -(len2+1), -1):
        cadena2_modif += cadena2[x]

print(cadena_modif)
print(cadena2_modif)
