"""
Pregunta 2

Alicia y Hugo, poseen una empresa de venta de alimentos para mascotas y le solicitan a ud, la realización de un programa informático. Puntualmente el sistema que le solicitan es de registro de ventas. Este registro se realiza al finalizar el día.

1-Se cargan facturas HASTA QUE el número de factura sea 0. (EL NUMERO DE FACTURA NO PUEDE SER NEGATIVO). Y una vez cargado el numero de la factura se carga el importe. (dos vectores)

2. Se muestran los números de facturas con sus importes

3- Se calcula el importe maximo facturado y a que factura pertenece. (Resolver con una función).

4. Calcular el promedio de los importes (Con una función), a partir del resultado obtenido reemplazar los números de facturas y los importes por el valor 9999 para todos aquellos que sean inferiores al promedio.

5. A partir del promedio de los importes, insertar después de cada valor superior al promedio, un -2 en ambos vectores

6. Se eliminan los números de facturas impares y los valores asociados a ellas

NOTA:
SE DEBE MOSTRAR EL RESULTADO DE TODO LO SOLICITADO

"""

"""
1.- no se validan ingresos de forma debida, hacer una funcion para hacer una lectura simple y append del valor leido no tiene sentido

2.- ok

3.- debe mostrarse en el ppal

4.- los reemplazos son siempre en el vector original, no se pueden generar vectores auxiliares para esto, y para mostrar los vectores hay una funcion q no se esta reutilizando

5.- no se puede hacer dentro de un for, te quedan elementos sin evaluar

6.- al hacer el eliminar dentro de un for, vas a evaluar elementos q no existen, se debe hacer en un while, manejando las posicione
"""

def validar(num):
    return num > 0

def carga_facturas(vec_fac, vec_imp):
    num_fact = int(input("Ingrese el numero de factura. Ingrese 0 para terminar:\t"))
    positivo = validar(num_fact)
    while num_fact != 0:
        if positivo:
            importe = int(input("Ingrese el importe de la factura %d:\t" %(num_fact)))
            vec_fac.append(num_fact)
            vec_imp.append(importe)
        else:
            print("Debe ingresar un numero mayor a cero o 0 para finalizar")
        num_fact = int(input("Ingrese el numero de factura:\t"))
        positivo = validar(num_fact)

def mostrar_fac_e_imp(vec_fac, vec_imp):
    leng_a = len(vec_fac)
    for i in range(0,leng_a):
        print("La factura Numero %d posee un importe de %d" %(vec_fac[i],vec_imp[i]))

def encontrar_maximo(vec_imp):
    leng_a = len(vec_imp)
    maximo = 0
    p_maximo = 0
    for i in range(0, leng_a):
        if i == 0 or vec_imp[i]>maximo:
            maximo = vec_imp[i]
            p_maximo = i
    return [maximo, p_maximo]

def calcular_prom(vec_imp):
    leng_a = len(vec_imp)
    acc = 0
    for i in range(0, leng_a):
        acc += vec_imp[i]
    promedio = acc / leng_a
    return promedio

def reemplazar_9999(vec_fac, vec_imp, promedio):
    leng_a = len(vec_imp)
    for i in range(0, leng_a):
        if vec_imp[i] < promedio:
            vec_imp[i] = 9999
            vec_fac[i] = 9999

def insertar_menos_2(vec_fac, vec_imp, promedio):
    i = 0
    while i < len(vec_imp):
        if vec_imp[i] > promedio:
            vec_imp.insert(i+1, -2)
            vec_fac.insert(i+1, -2)
            i+=1
        i += 1

def eliminar_impares(vec_fac, vec_imp):
    i = 0
    while i < len(vec_fac):
        if vec_fac[i] % 2 != 0:
            vec_fac.pop(i)
            vec_imp.pop(i)
            i = 0
        if vec_fac[i] % 2 == 0:
            i += 1 # aumentar es lo ULTIMO que se hace
        

def programa():
    facturas = []
    importes = []
    carga_facturas(facturas, importes)
    mostrar_fac_e_imp(facturas, importes)
    maximo_pmaximo = encontrar_maximo(importes)
    maximo = maximo_pmaximo[0]
    p_maxi = maximo_pmaximo[1]
    print("El importe maximo es de %d y corresponde a la factura %d" %(maximo, facturas[p_maxi]))
    averag = calcular_prom(importes)
    print("El promedio de los importes es de %d" %(averag))
    reemplazar_9999(facturas, importes, averag)
    print("Luego del reemplazo por 9999 los valores son:")
    mostrar_fac_e_imp(facturas, importes)
    insertar_menos_2(facturas, importes, averag)
    print("Luego del reemplazo por -2 los valores son:")
    mostrar_fac_e_imp(facturas, importes)
    eliminar_impares(facturas, importes)
    print("Luego de eliminar las facturas impares, los valores son:")
    mostrar_fac_e_imp(facturas, importes)

programa()