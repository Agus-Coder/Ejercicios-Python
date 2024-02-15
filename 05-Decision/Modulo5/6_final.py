numero_viaje = int(input("Ingrese el numero de viaje: \n"))
total = 0
total_viajs = 0
viajes_c1 = 0 
viajes_c2 = 0
viajes_c3 = 0
horas_c1 = 0 
horas_c2 = 0
horas_c3 = 0
total_interior = 0

while numero_viaje != 0:
    numero_camion = int(input("Ingrese el numero de camion: \n"))

    while numero_camion < 1 or numero_camion > 3:
        print("numero ingresado: ", numero_camion)
        numero_camion = int(input("Numero de camion incorrecto. Ingrese 1, 2 o 3: \n"))
        
    horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas: \n"))
    
    destino_opcion = int(input("Ingrese el destino: \n1 - Capital\n2 - Interior\n"))
    while destino_opcion < 1 or destino_opcion > 2:
        destino_opcion = int(input("Destino incorrecto. Ingrese 1 o 2: \n"))
    

    if numero_camion == 1:
        total += horas_trabajadas * 150
        horas_c1 += horas_trabajadas
        viajes_c1 += 1
    elif numero_camion ==2:
        total += horas_trabajadas * 200
        horas_c2 += horas_trabajadas
        viajes_c2 += 1
    else:
        total += horas_trabajadas * 300
        horas_c3 += horas_trabajadas
        viajes_c3 += 1

    total_viajs += 1

    if destino_opcion == 2:
        total_interior +=1

    numero_viaje = int(input("Ingrese el numero de viaje: \n"))

print(f"Total recaudado: {total}\nTotal viajes: {total_viajs}\nViajes Camion 1:{viajes_c1}\nViajes Camion 2:{viajes_c2}\nViajes Camion 3:{viajes_c3}\nHoras Camion 1:{horas_c1}\nhoras Camion 2:{horas_c2}\nhoras Camion 3:{horas_c3}\nViajes al interior: {total_interior}\n")