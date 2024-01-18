semana = int(input("Ingrese el numero de semana: \n"))
gasto = 0
while semana != 5:
    gasto += int(input("Ingrese el gasto semanal: \n"))
    semana = int(input("Ingrese el numero de semana: \n"))

promedio = gasto / 4

print("El gasto promedio semanal es de: ", promedio, " Pesos")
