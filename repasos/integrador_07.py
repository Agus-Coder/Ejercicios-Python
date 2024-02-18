def cargar_array(arr):
    number = 0
    for i in range(0,13):
        data_in = int(input("Ingrese un numero:\n"))
        if i ==0:
            number = data_in
        if i > 0:
            arr.append(number*data_in)

def mostrar_arreglo(arr):
    leng_a = len(arr)
    for i in range(0,leng_a):
        print("Posicion %d: %d" %(i, arr[i]))

def multiplos_de_4(arr):
    leng_a = len(arr)
    acc = 0
    for i in range(0, leng_a):
        if arr[i] % 4 == 0:
            acc +=1
    return acc

def producto_pares(arr):
    leng_a = len(arr)
    acc = 1
    for i in range(0, leng_a):
        if i % 2 == 0:
            acc *= arr[i]
    return acc

def suma_hasta_3(arr):
    leng_a = len(arr)
    acc = 0
    for i in range(0,leng_a):
        if arr[i] % 3 != 0:
            acc += arr[i]
        if arr[i] % 3 == 0:
            acc += arr[i]
            return acc
        if i == leng_a -1:
            print("No hay multiplos de 3 en el arreglo")
            return acc

def encontrar_maximo(arr):
    leng_a = len(arr)
    max = 0
    for i in range(0,leng_a):
        if i==0 or arr[i]>max :
            max = arr[i]
    return max

def agregar_consecutivo(arr, max):
    consec = max + 1
    arr.append(consec)


def programa():
    array = []
    cargar_array(array)
    mostrar_arreglo(array)
    multiplos_4 = multiplos_de_4(array)
    prod_par = producto_pares(array)
    suma_3 = suma_hasta_3(array)
    print("la cantidad de multiplos de 4 encontrados es de %d.\nEl producto de las posiciones pares es de %d.\n La suma hasta le primer multiplo de 3 es de %d" %(multiplos_4, prod_par, suma_3))
    maximo = encontrar_maximo(array)
    print("El maximo en el arreglo es %d" %(maximo))
    agregar_consecutivo(array, maximo)
    mostrar_arreglo(array)
    array.sort()
    mostrar_arreglo(array)

programa()