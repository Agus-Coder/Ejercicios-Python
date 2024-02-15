cantidad_empanadas = int(input("Ingrese la cantidad de empanadas: \n"))

total_global = 0
horno_total = 0
fritas_total = 0
dulces_total = 0
max_empanadas = 0
max_direccion = ''

while cantidad_empanadas != 0:
    direccion = input("Ingrese su domicilio: \n")
    disponibles = cantidad_empanadas

    if cantidad_empanadas >= max_empanadas:
        max_direccion = direccion
        max_empanadas = cantidad_empanadas

    total = 0
    horno = 0
    fritas = 0
    dulces = 0
    
    while disponibles >0:
        tipo = int(input("Ingrese el tipo de empanda: 1 horno, 2 frita 3 dulce\n"))
        while tipo < 1 or tipo >3:
            tipo = int(input("Ingrese el tipo de empanda: 1 horno, 2 frita 3 dulce\n"))
        cantidad = int(input(f"Ingrese la cantidad de empanadas de este tipo, le quedan {disponibles} para elegir\n"))

        while cantidad > disponibles:
            cantidad = int(input(f"No posee esa cantidad disponible, debe ingresar {disponibles} o menos\n"))
        
        if cantidad <= disponibles:
            if tipo == 1:
                horno += cantidad
                total += cantidad * 18
                print(f"Agregada/s {cantidad} empanada/s al horno")
            if tipo == 2:
                fritas += cantidad
                total += cantidad * 19
                print(f"Agregada/s {cantidad} empanada/s fritas")
            if tipo == 3:
                dulces += cantidad
                total += cantidad * 21
                print(f"Agregada/s {cantidad} empanadas dulce/s")
            disponibles -= cantidad

    total_global += total
    horno_total += horno
    fritas_total += fritas
    dulces_total += dulces

    if cantidad_empanadas >= 15:
        print(f"El cliente en {direccion} compro 15 o mas empanadas")
    
    cantidad_empanadas = int(input("Ingrese la cantidad de empanadas: \n"))

print(f"El cliente que compro mas empanas es el de la direccion {max_direccion} y compro {max_empanadas}\nSe vendieron {horno_total} empanadas al horno, {fritas_total} empanadas fritas y {dulces_total} empanadas dulces. El total recaudado fue de {total_global} pesos")