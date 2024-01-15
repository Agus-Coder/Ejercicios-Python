codigoLlamada = int(input("Ingrese 1 para llamada local, 2 para llamada interurbana y 3 para internacional "))

if codigoLlamada == 1:
    costoMinuto = 0.25
    duracion = int(input("Ingrese la duracion de la llamada "))
    costoTotal = costoMinuto * duracion
    print("El costo total es: ", costoTotal, " pesos")
elif codigoLlamada == 2:
    costoMinuto = 0.40
    duracion = int(input("Ingrese la duracion de la llamada "))
    costoTotal = costoMinuto * duracion
    print("El costo total es: ", costoTotal, " pesos")
elif codigoLlamada == 3:
    costoMinuto = 1.05
    duracion = int(input("Ingrese la duracion de la llamada "))
    costoTotal = costoMinuto * duracion
    print("El costo total es: ", costoTotal, " pesos")
