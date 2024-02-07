numero = int(input("Ingrese el numero: \n"))
positivos = 0
while numero != 0:
    if numero >0:
        positivos += 1
    numero = int(input("Ingrese el numero: \n"))

print("La cantidad de positivos es: ", positivos)