"""
Se quiere llevar el control de ventas de dos productos tazas y termos. Se guardan las cantidades vendidas en una semana. Para ello se cargan dos arreglos uno por cada producto.Las tazas tienen un precio de $1750 y los termos de $8075.
La carga finaliza con cantidad = 0, y puede haber mas de una venta por día
Se pide:
· Ingresar el tipo de producto TZ para tazas y TE para termos.
· Ingresar la cantidad vendida según el producto seleccionado.
· Realizar una función que calcule el máximo de ventas en cantidad para un producto dado y mostrar el monto correspondiente.
· Calcular el promedio semanal vendido en cantidad.
· Validar los datos de entrada, no permitir cantidades negativas.
"""

def cargar_ventas(vec_tz, vec_te):
    cantidad = int(input("Ingrese la cantidad de productos vendidos:\t"))
    while cantidad != 0:
        tipo = input("Ingrese el tipo de producto, TZ para tazas y TE para termos:\t")
        while tipo != 'TE' and tipo != 'TZ':
            tipo = input("Debe ingresar TE o TZ:\t")
    
        if tipo == 'TE':
            vec_te.append(cantidad)
        if tipo == 'TZ':
            vec_tz.append(cantidad)
        
        cantidad = int(input("Ingrese la cantidad de productos vendidos:\t"))

def encontrar_maximo(vec):
    leng_a = len(vec)
    maximo = 0
    for i in range(0, leng_a):
        if i == 0 or vec[i] > maximo:
            maximo = vec[i]
    return maximo

def comparar_maximos(maxi_tz, maxi_te):
    if maxi_tz > maxi_te:
        total = maxi_tz * 1750
        print("El maximo de ventas corresponde a %d tazas por un total de %d$" %(maxi_tz, total))
    if maxi_tz < maxi_te:
        total = maxi_te * 8075
        print("El maximo de ventas corresponde a %d termos por un total de %d$" %(maxi_tz, total))

def promedio_semanal(vec_tz, vec_te):
    leng_tz = len(vec_tz)
    leng_te = len(vec_te)
    total = leng_tz + leng_te
    acc = 0
    for i in range(0, leng_tz):
        acc += vec_tz[i]
    for i in range(0, leng_te):
        acc += vec_te[i]
    
    promedio = acc//total
    return promedio


def programa():
    tazas = []
    termos = []
    cargar_ventas(tazas, termos)
    maximo_tazas = encontrar_maximo(tazas)
    maximo_termos = encontrar_maximo(termos)
    comparar_maximos(maximo_tazas, maximo_termos)
    prom_sem = promedio_semanal(tazas, termos)
    print("El promedio semanal es de %d ventas" %(prom_sem))

programa()