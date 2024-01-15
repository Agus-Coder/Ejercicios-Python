cadena = input("Ingrese algo con mas de 5 caracteres ")
cadena2 = ""

long = len(cadena)

for x in range(0, long-1):
    if x != long:
        cadena2 += cadena[x] + ","

cadena2 += cadena[long-1]

print(cadena2)
