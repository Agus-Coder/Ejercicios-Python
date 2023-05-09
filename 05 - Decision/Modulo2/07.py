edad1 = int(input("Ingrese la edad de la primer persona: "))
edad2 = int(input("Ingrese la edad de la segunda persona: "))

if edad1 < 18 and edad2 > 18 or edad1 > 18 and edad2 < 18:
    promedio = (edad1 + edad2)/2
    print("El promedio de edades es: ", promedio)
else:
    print("Las edades son: ", edad1, " y ", edad2)
