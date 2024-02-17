def carga_pares():
    arreglo = []
    for i in range(1,11):
        arreglo.append(2*i)
    return arreglo

def carga_cincos():
    arreglo = []
    for i in range(10,0,-1):
        arreglo.append(5*i)
    return arreglo

def suma_vectores(arr1,arr2):
    arr3 = []
    for i in range(0,10):
        sum = arr1[i] + arr2[i]
        arr3.append(sum)
    return arr3

def cargar_vector(arr1, arr2):
    arr3 = []
    for i in range(0,10):
        arr3.append(arr1[i])
    for i in range(0,10):
        arr3.append(arr2[i])
    return arr3

def inversion_vector(arr1):
    arr1.reverse()
    return arr1

def find_max(arr1):
    max = 0
    pmax = 0
    long = len(arr1)
    for i in range(0, long):
        if (i == 0 or arr1[i] > max):
            max = arr1[i]
            pmax = i
    return [max,pmax]

def replace_by_zero(arr1,index):
    lenga = len(arr1)
    for i in range(index+1, lenga):
        arr1[i] = 0
    return arr1

def average(arr1):
    sum = 0
    lenga = len(arr1)
    for i in range(0,lenga):
        sum+=arr1[i]
    average = sum/lenga
    return average


def compare_average(arr1,number):
    lenga = len(arr1)
    total = 0
    for i in range(0,lenga):
        if arr1[i]>number:
            total+=1
    return total


def program():
    a = carga_pares()
    a_inv = carga_pares()
    b = carga_cincos()
    [max_b,pos_max_b] = find_max(b)
    c = suma_vectores(a,b)
    d = cargar_vector(a,b)
    inversion_vector(a_inv)
    b_zeros = replace_by_zero(b,pos_max_b)
    ave_c = average(c)
    above_average_c = compare_average(c,ave_c)

    print("El Vector A es \t") 
    print(a)
    print("\n")
    print("El vector B es \t") 
    print(b)
    print("\n")
    print("El vector C es \t") 
    print(c)
    print("\n")
    print("El vector d es \t") 
    print(d)
    print("\n")
    print("El vector a invertido es \t")
    print(a_inv)
    print("\n")
    print("El maximno de B es %d en la posicion %d" %(max_b, pos_max_b))
    print("\n")
    print("B con ceros luego del maximo es \t")
    print(b_zeros)
    print("\n")
    print("El promedio de C es %d. Hay %d numeros por encima del promedio" %(ave_c, above_average_c))



program()