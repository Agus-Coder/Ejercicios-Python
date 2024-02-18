def cargar_vector(vector):
    for i in range(100):
        vector.append(int(input(f'Ingrese rendimiento N°{i+1}: ')))
 
 
def mostrar_vector(vector):
    for i in range(len(vector)):
        print(f'Rendimiento N°{i+1}: {vector[i]}\n')
        
def promediar(vector):
    total=len(vector)
    if total>0:
        suma=0
        for valor in vector:
            suma+=valor
        return suma/total
    else:
        print("No hay valores para promediar.\n")
        
def sumar_sobre_prom(vector, promedio):
    suma = 0
    for i in range(len(vector)):
        if vector[i] > promedio:
            suma+=vector[i]
    return suma
 
 
def hallar_max(vector):
    for i in range(len(vector)):
        if i == 0:
            maximo=vector[i]
        elif vector[i]>maximo:
            maximo=vector[i]
    return maximo
    
def hallar_min(vector):
    for i in range(len(vector)):
        if i == 0:
            minimo=vector[i]
        elif vector[i]<minimo:
            minimo=vector[i]
    return minimo
    
def es_par(valor):
    if valor % 2 == 0:
        return True
    else:
        return False
        
def insertar_par_impar(vector, maximo, minimo):
    if es_par(maximo) and es_par(minimo):
        vector.append(999)
    elif (not es_par(maximo)) and (not es_par(minimo)):
        i = 0
        while i < len(vector):
            if (not es_par(vector[i])):
                vector.insert(i+1, 333)
                i+=1
            i+=1
 
 
def insertar_medio(vector,valor):
    pos_medio=len(vector)//2
    vector.insert(pos_medio, valor)
 
 
def eliminar_por_pos(vector, pos):
    vector.pop(pos)
 
 
def ordenar_desc(vector):
    for i in range(len(vector)):
        for j in range(i+1, len(vector)):
            if vector[i]<vector[j]:
                aux=vector[i]
                vector[i]=vector[j]
                vector[j]=aux
 
 
rendimiento = []
 
 
cargar_vector(rendimiento)
 
 
if len(rendimiento)>0:
    print("Registro de Desempeño:\n")
    mostrar_vector(rendimiento)
    prom=promediar(rendimiento)
    if prom:
        print(f'Estadísticas de Desempeño: \nEl promedio de rendimiento es {prom}.\n\n')
        supera_promedio_suma=sumar_sobre_prom(rendimiento, prom)
        print(f'Análisis de Desempeño Sobresaliente: \nLa suma de los valores que superan el promedio es {supera_promedio_suma}.\n')
    maxi=hallar_max(rendimiento)
    print(f'El rendimiento máximo es {maxi}.\n')
    mini=hallar_min(rendimiento)
    print(f'El rendimiento mínimo es {mini}.\n')
    insertar_par_impar(rendimiento, maxi, mini)
    print("Rendimiento modificado, si máximo y mínimo son ambos par o impar:\n\n")
    mostrar_vector(rendimiento)
    print("Optimización del Vector:\n")
    print("Insertar el resultado de la suma de los valores superiores al promedio en la mitad del vector de rendimiento.\n")
    print("Eliminar el segundo y cuarto elemento del vector de rendimiento.:\n\n")
    insertar_medio(rendimiento,supera_promedio_suma)
    eliminar_por_pos(rendimiento, 3)
    eliminar_por_pos(rendimiento, 1)
    mostrar_vector(rendimiento)
    print("Ordenamiento del Vector: Descendente\n")
    ordenar_desc(rendimiento)
    mostrar_vector(rendimiento)
else:
    print("No se cargaron datos.")