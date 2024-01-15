print("Por favor, las instrucciones que se indicaran a continuacion")

grado1 = int(input("Ingrese los grados del primer angulo"))
min1 = int(input("Ingrese los minutos del primer angulo"))

if min1<0 or min1>=60:
    print("ingresar valores de minutos mayores a cero y menores a 60")

seg1 = int(input("Ingrese los segundos del primer angulo"))

if seg1<0 or seg1>=60:
    print("ingresar valores de segundos mayores a cero y menores a 60")

grado2 = int(input("Ingrese los grados del segundo angulo"))
min2 = int(input("Ingrese los minutos del segundo angulo"))

if min2<0 or min2>=60:
    print("ingresar valores de minutos mayores a cero y menores a 60")

seg2 = int(input("Ingrese los segundos del segundo angulo"))

if seg2<0 or seg2>=60:
    print("ingresar valores de segundos mayores a cero y menores a 60")

segTotal = seg1 + seg2
minTotal = min1 + min2
gradoTotal = grado1 + grado2

