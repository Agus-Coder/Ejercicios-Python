'''
Leer 20 números y cargarlos en un vector.
1) Calcular cual es el máximo de ese vector (de manera programática)
2) Calcular el promedio del vector/array
3) Generar otro vector con los números pares del vector original
4) Calcular el mínimo del vector generado (El vector de los pares)
5) En el vector de los pares, insertar después de cada valor superior al promedio del punto 2 el número 999
6) Elimine del segundo vector (pares) el número 4, contemplar que en el caso de no existir dicho numero
eliminar el número que se encuentra en la primer posición. Generar dos funciones, una que reciba un vector 
y un número entero (la cantidad de valores a ingresar), y cargue valores impares múltiplos de 4
Y la segunda, que busque si existe el valor 24, pero al encontrarlo se debe detener la búsqueda y no llegar
hasta el final del vector. Y retornar la leyenda "Lo encontré" o "No lo encontré", según corresponda.
'''

def cargar_vector(vec):
    for i in range(0,20):
        number = int(input("Ingrese un numero para cargar en array\t"))
        vec.append(number)

def encontrar_maximo(vec):
    leng_a = len(vec)
    maximo = 0
    for i in range(0, leng_a):
        if i == 0 or vec[i] > maximo:
            maximo = vec[i]
    return maximo

def calcular_promedio(vec):
    leng_a = len(vec)
    acc = 0
    for i in range(0, leng_a):
        acc += vec[i]
    promedio = acc / leng_a
    return promedio

def obtener_pares(vec):
    leng_a = len(vec)
    pares  = []
    for i in range(0, leng_a):
        number = vec[i]
        if number % 2 == 0:
            pares.append(number)
    return pares

def encontrar_minimo(vec):
    leng_a = len(vec)
    minimo = 0
    for i in range(0, leng_a):
        if i == 0 or vec[i] < minimo:
            minimo = vec[i]
    return minimo

def insertar_999(vec,prom):
    i = 0
    while i < len(vec):
        if vec[i] > prom:
            vec.insert(i+1,999)
            i+=1
        i+=1

def eliminar_4(vec):
    while 4 in vec:
        vec.remove(4)
    if not 4 in vec:
        vec.pop(0)

def cargar_numeros(vec, cant):
    valor = 1
    while cant > 0:
        if valor % 2 != 0 and valor % 4 ==0:
            vec.append(valor)
            cant -=1
        valor +=1

def encontrar_24(vec):
    leng_a = len(vec)
    for i in range(0, leng_a):
        if vec[i] == 24:
            print("Lo encontre")
            return
        print("No lo encontre")
        return
def mostar_vector(vec):
    leng_a = len(vec)
    for i in range(0,leng_a):
        print("Posiccion %d, valor %d" %(i, vec[i]))

def programa():
    numeros = []
    cargar_vector(numeros)
    mostar_vector(numeros)
    maximo = encontrar_maximo(numeros)
    print("El maximo numero encontrado es %d" %(maximo))
    promedio = calcular_promedio(numeros)
    print("El numero promedio es %d" %(promedio))
    pares = obtener_pares(numeros)
    mostar_vector(pares)
    minimo_pares = encontrar_minimo(pares)
    print("El mini numero encontrado en el vector de pares es %d" %(minimo_pares))
    insertar_999(pares,promedio)
    eliminar_4(pares)
    mostar_vector(pares)
    #Explicacion porque no se ejecuta dicha funcion
    # cargar_numeros
    encontrar_24(pares)

programa()
