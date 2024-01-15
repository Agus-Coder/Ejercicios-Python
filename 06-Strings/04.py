cadena = input("Ingrese algo con mas de 5 caracteres ")
cadena2 = ""

long = len(cadena) -1

## range() requiere un tercer argumento para indicar un orden reverso de ejecucion

for x in range(long, -1, -1): ##el segundo -1 va porque un 0 no inluiria al primer caracter
    cadena2 += cadena[x]

print(cadena2)
