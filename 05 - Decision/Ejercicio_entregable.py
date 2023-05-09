# Arana Agustin, Introduccion a la Programacion - Ingenieria informatica

ciudad_filial = ''
capacidad_hotel = 0
cantidad_hab = 0
huespesdes_mes = 0

hotel_max_habit = 0
nombre_max_habit = ''

huespedes_totales = 0

for i in range(1, 11):
    ciudad_filial = input('Ingrese el nombre de la ciudad de la filial')
    capacidad_hotel = int(input('ingrese la capacidad del hotel'))
    cantidad_hab = int(input('ingrese la cantidad de habitaciones'))
    huespesdes_mes = int(input('ingrese la cantidad de huespedes en un mes'))

    huespedes_totales += capacidad_hotel

    if i == 1 or cantidad_hab > hotel_max_habit:
        hotel_max_habit = cantidad_hab
        nombre_max_habit = ciudad_filial

    porcentaje_ocup = huespesdes_mes/capacidad_hotel * 100

    print("El hotel ", i, " ubicado en ", ciudad_filial,
          " posee un porcentaje de ocupacion del ", porcentaje_ocup, "%")


print('Toda la cadena de hoteles puede alojar un total de ',
      huespedes_totales, ' huespedes')
print("El nombre de la ciudad con la mayor cantidad de habitaciones es: ",
      nombre_max_habit)
