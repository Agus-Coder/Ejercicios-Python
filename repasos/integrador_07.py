def generar_array(arr):
    number = 0
    for i in range(0,13):
        data_in = int(input("Ingrese un numero:\n"))
        if i ==0:
            number = data_in
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
        if arr[i] % 2 == 0:
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

