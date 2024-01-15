max = 0
mas_de_20 = 0
menos_de_5_cat_1 = 0
sueldos_cat_1 = 0
sueldos_cat_2 = 0
sueldos_cat_3 = 0
sueldos_totales = 0
nombre_max = ''

for i in range(1, 10):
    nombre = input("ingrese el nombre del empleado")
    sueldo = int(input("ingrese el sueldo del empleado"))
    cat = int(input("ingrese la categoria del empleado"))\
    

    if i == 1:
        max = sueldo
        nombre_max = nombre
        print(nombre_max, " es el empleado que mas gana. Su sueldo es de: ", sueldo)

    if sueldo > 20000:
        mas_de_20 += 1

    if sueldo < 5000 and cat == 1:
        menos_de_5_cat_1 += 1

    if sueldo > max:
        max = sueldo
        nombre_max = nombre
        print(nombre, " es el empleado que mas gana. Su sueldo es de: ", sueldo)

    if cat == 1:
        sueldos_cat_1 += sueldo
    if cat == 2:
        sueldos_cat_2 += sueldo
    if cat == 3:
        sueldos_cat_3 += sueldo

    sueldos_totales += sueldo

print("El total de sueldos a pagar es: ", sueldos_totales)
print("la cantidad de empleados que ganan mas de 20 mil es: ", mas_de_20)
print("la cantidad de empleados que ganan menos de 20 mil y son categoria 1 son: ", menos_de_5_cat_1)

print("El total de sueldos a pagar categoria 1 es: ", sueldos_cat_1)
print("El total de sueldos a pagar categoria 2 es: ", sueldos_cat_2)
print("El total de sueldos a pagar categoria 3 es: ", sueldos_cat_3)

print(nombre_max, " es el empleado que mas gana. Su sueldo es de: ", max)
