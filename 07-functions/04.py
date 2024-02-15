def superficie (b, h):
    sup = b*h
    return sup

def costo_alf(sup):
    total = 104 * sup
    return total

def pintar(sup):
    total =83 * sup / 6
    return total

def perimetro(largo, ancho):
    per = 2*(largo + ancho)
    return per

def programa():
    alto = int(input("Ingrese altura de las paredes\n"))
    ancho = int(input("Ingrese ancho del ambiente\n"))
    largo = int(input("Ingrese largo del ambiente\n"))

    pared_corta = superficie(alto, ancho)
    pared_larga = superficie(alto, largo)
    piso = superficie(ancho, largo)
    total_paredes = 2*(pared_corta + pared_larga)
    per = perimetro(ancho, largo)
    total_pintura = pintar(total_paredes)
    total_alf = costo_alf(piso)

    print(f"La superficie del piso es de {piso} m2.\nLa superficie de las paredes es de {total_paredes} m2.\nEl perimetro del ambiente es de {per} m.\nEl costo de alfombrar el ambiente es de {total_alf}$.\nEl costo de pintar el ambiente es de {total_pintura}$")

programa()