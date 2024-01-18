print("-------------- Ejercicio 1 --------------")
valor_hora = int(input("Ingrese el valor hora del trabajador" ))
horas_trabajo = int(input("Ingrese la cantidad de horas trabajadas en el mes: "))

print("El sueldo del trabajador es: %d dolares mensuales" %(valor_hora * horas_trabajo))

print("-------------- Ejercicio 2 --------------")
#monto_total = int(input("Ingrese el valor de la heladera"))

#print("El costo en efectivo es %d" %(monto_total*0.9))

print("-------------- Ejercicio 4 --------------")

#lado1 = int(input("Ingrese el lado 1:\n"))
#lado2 = int(input("Ingrese el lado 2:\n"))

#h = (lado1**2 + lado2**2)** 0.5

#print("La hipotenusa mide", h);

print("-------------- Ejercicio 5 --------------")

#tres_dig = int(input("Ingrese el numero de tres digitos:\n"))
#resto = tres_dig % 100
#segundo_dig = resto // 10

#print("El segundo digito es", segundo_dig);

print("-------------- Ejercicio 6 --------------")
# number = int(input("Ingrese un numero:\n"))
# 
# if number > 0:
    # output = number ** 0.5
    # print("La razin cuadrada del numero es: \t", output)
# elif number < 0:
    # output = number ** 2
    # print("El cuadrado del numero es: \t", output)
# elif number == 0:
    # output = "Error, ha ingresado un valor nulo"
    # print(output)


print("-------------- Ejercicio 7 --------------")

# edad1 = int(input("Ingrese la edad 1:\n"))
# edad2 = int(input("Ingrese la edad 2:\n"))
# 
# if edad1>= 18 and edad2 <18 or edad2>= 18 and edad1 <18:
    # promedio = (edad1 + edad2)/2
    # print(promedio)
# else:
    # print(edad1)
    # print(edad2)

print("-------------- Ejercicio 8 --------------")

# number1 = int(input("Ingrese un primer numero:\n"))
# number2 = int(input("Ingrese un segundo numero:\n"))
# 
# if number2 == 0:
    # print("No se puede realizar el cociente")
# else:
    # print("El cociente es: \n", number1/number2)

print("-------------- Ejercicio 9 --------------")

# ganancias = int(input("Ingrese las ganancias anuales:\n"))

# if ganancias <= 10000:
#     retenciones = 0
# elif ganancias > 10000 and ganancias <= 15000:
#     retenciones = 0.02 * (ganancias - 10000)
# elif ganancias > 15000:
#     retenciones = 300 + 0.05 * (ganancias - 15000)

# print("Las retenciones totales a cobrar son de ", retenciones, ". pesos")

print("-------------- Ejercicio 10 --------------")

# print("Piense en MM, ML o LM")

# homb_o_m = int(input("Su personaje es mujer? 1 si, 2 no:\n"))

# if homb_o_m == 1:
#     print("Esta pensando en ML")
# else:
#     profesion = int(input("Su personaje es futbolista? 1 si, 2 no:\n"))
#     if profesion == 1:
#         print("Esta pensando en LM")
#     else:
#         print("Esta pensando en MM")
        
print("-------------- Ejercicio 14 --------------")

# mayor = int(input("Ingrese un numero de dos digitos:\n"))

# unidad  = (mayor/10) % 1
# decena = (mayor/10) // 1
# decena2 = unidad * 100
# final = decena + decena2


# if mayor > 50:
#     print(final)
# else:
#     print(unidad*10)

print("-------------- Ejercicio 17 --------------")

g1 = int(input("Ingrese primer grado:\n"))
m1 = int(input("Ingrese primer minuto:\n"))
s1 = int(input("primer segundo:\n"))

g2 = int(input("g2:\n"))
m2 = int(input("m2:\n"))
s2 = int(input("segundo:\n"))


g3 = g2 + g1
m3 = m2 + m1
s3 = s2 + s1

if s3 >= 60:
    s3 -= 60
    m3 += 1
if m3 >=60:
    m3 -= 60
    g3 +=1

print(g3, m3, s3)