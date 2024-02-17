def cargar_numeros(arr):
    for i in range(0,9):
        if i % 2 == 0:
            number = int(input("Ingrese un numero par:\t"))
            while(number % 2 != 0):
                number = int(input("Ingrese un numero par:\t"))
            arr.append(number)
        if i % 2 != 0:
            number = int(input("Ingrese un numero negativo:\t"))
            while(number >= 0):
                number = int(input("Ingrese un numero negativo:\t"))
            arr.append(number)

def invertir_arreglo(arr):
    leng_a = len(arr)
    inversed = []
    for i in range(leng_a-1, -1, -1):
        inversed.append(arr[i])
    print(inversed)
    return inversed

def mitad(num):
    return num/2

def positivo(num):
    if num < 0:
        return -num

def inc_b(arr):
    new_arr = []
    for i in range(0,9):
        if i % 2 == 0:
            new_arr.append(mitad(arr[i]))
        if i % 2 != 0:
            new_arr.append(positivo(arr[i]))
    return new_arr

def ordenar(arr):
    arr.sort()
    print(arr)

def eliminar(arr):
    leng_a = len(arr)
    counter = 0
    while counter < leng_a:
        if arr[counter] % 4 == 0:
            arr.remove(arr[counter])
            counter = 0
            leng_a = len(arr)
        counter += 1
    print(arr)

def programa():
    arreglo = []
    cargar_numeros(arreglo)
    invertido = invertir_arreglo(arreglo)
    arrgeglo_2 = inc_b(arreglo)
    print(arrgeglo_2)
    ordenar(invertido)
    eliminar(arreglo)

programa()