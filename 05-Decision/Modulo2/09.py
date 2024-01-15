gananciaEmpresa = int(input("Ingrese la ganancia anual de la empresa"))

retencion = 0

if gananciaEmpresa <= 10000:
    print("La empresa no tiene retenciones")
elif gananciaEmpresa > 10000 and gananciaEmpresa <= 15000:
    retencion = 0.02 * (gananciaEmpresa - 10000)
    print("La retencion total es de: ", retencion)
elif gananciaEmpresa > 15000:
    retencion = 300 + 0.05 * (gananciaEmpresa - 15000)
    print("La retencion total es de: ", retencion)
