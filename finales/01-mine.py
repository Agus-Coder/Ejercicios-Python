def registro():
    vec = []
    for i in range(0,10):
        empleado = i + 1
        number = int(input("Ingrese el rendimiento del empleado %d:\t" %(empleado)))
        vec.append(number)
    return vec

def mostrar_vector(vec):
    leng_a = len(vec)
    for i in range (0, leng_a):
        print(vec[i])

def promedio(vec):
    leng_a = len(vec)
    acc = 0
    for i in range (0, leng_a):
        acc += vec[i]
    promedio = acc / leng_a
    print("El promedio de rendimiento de los empleado es %d" %(promedio))
    return promedio

def suma_may_prom(vec, prom):
    leng_a = len(vec)
    acc = 0
    for i in range (0, leng_a):
        if vec[i] > prom:
            acc += vec[i]
    print("La suma de los resultados mayores al promeido es de %d" %(acc))
    return acc

def max_y_min(vec):
    leng_a = len(vec)
    max = 0
    min = 0
    for i in range (0, leng_a):
        if i == 0 or vec[i] > max:
            max = vec[i]
        if i == 0 or vec[i] < min:
            min = vec[i]
    print("El rendimiento maximo obtenido es de %d, mientras que el minimo obtenido es de %d" %(max, min))
    return [min, max]

def insertar(vec, max, min):
    if max % 2 == 0 and min % 2 == 0:
        vec.append(999)
    if max % 2 != 0 and min % 2 != 0:
        insertar_333(vec)

def insertar_333(vec):
    i = 0
    while i < len(vec):
        if vec[i] % 2 !=0:
            vec.insert(i+1,333)
            i+=1
        i+=1

def insertar_en_mitad(vec,sum):
    mitad = len(vec)//2
    centro = mitad - 1
    vec.insert(centro, sum)

def eliminar_posiciones(vec):
    vec.pop(1)
    vec.pop(2)

def ordenar(vec):
    for i in range (len(vec)):
        for j in range (i+1,len(vec)):
            if vec[i] < vec[j]:
                aux = vec[i]
                vec[i] = vec[j]
                vec[j] = aux


def programa():
    # Inciso A
    desempeno = registro()
    mostrar_vector(desempeno)
    # Inciso B
    average = promedio(desempeno)
    # Inciso C
    sum_mayores = suma_may_prom(desempeno,average)
    min_max = max_y_min(desempeno)
    insertar(desempeno,min_max[1], min_max[0])
    insertar_en_mitad(desempeno,sum_mayores)
    eliminar_posiciones(desempeno)
    mostrar_vector(desempeno)
    ordenar(desempeno)
    mostrar_vector(desempeno)

programa()