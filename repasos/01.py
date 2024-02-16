def cargar_numeros(arr):
    for i in range(0,15):
        number = int(input("ingrese un numero:\t"))
        arr.append(number)


def repetir_primero(arr):
    leng_a = len(arr)
    while leng_a<8:
        arr.append(arr[0])
        leng_a = len(arr)
    return arr

def ordenar_numeros(arr1, arr2, arr3):
    leng_a = len(arr1)
    for i in range(0,leng_a):
        leng_b = len(arr2)
        if arr1[i]>20 and leng_b <8:
            arr2.append(arr1[i])
        if arr1[i]<=20:
            arr3.append(arr1[i])
    if leng_b < 8:
        arr2 = repetir_primero(arr2)

def calcular_promedio(men_20):
    leng_a = len(men_20)
    acc = 0
    for i in range(0, leng_a):
        acc += men_20[i]
    average = acc / leng_a
    return average

def maximo(may_20):
    leng_a = len(may_20)
    max = 0
    pmax = 0
    for i in range(0,leng_a):
        if i==0 or may_20[i]>max:
            max = may_20[i]
            pmax = i
    return[max,pmax]

def factorial_par(may_20):
    leng_a = len(may_20)
    for i in range(0,leng_a):
        if i % 2 == 0:
            acc = 1
            for j in range(1, may_20[i]):
                acc *= j
            print("Factorial de numero %d : %d" %(may_20[i],acc))

def terminar(may_20,men_20):
    leng_a = len(may_20)
    if leng_a >0:
        promedio = calcular_promedio(men_20)
        maximo_posicion = maximo(may_20)
        posicion_anterior = (maximo_posicion[1]-1)
        anterior_al_maximo = may_20[posicion_anterior]
        print("El promedio de los numeros que no entraron al arreglo es de %d" %(promedio))
        print("el numero %d es el que se encuentra anterior al maximo del arreglo" %(anterior_al_maximo))
        factorial_par(may_20)
    else:
        print("No se han ingresado numeros mayores a 20")

    

def program():
    array_inicial = []
    array_mayor_20 = []
    array_menor_20 = []
    cargar_numeros(array_inicial)
    ordenar_numeros(array_inicial, array_mayor_20, array_menor_20)
    terminar(array_mayor_20, array_menor_20)


program()