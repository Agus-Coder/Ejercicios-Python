cadena = input("Ingrese algo con mas de 5 caracteres ");

print(cadena[0:2]) # el ultimo espacio no es considerado

leng = len(cadena)
al_reves = ''
for x in range(-1, -leng, -1):
    al_reves += cadena[x]

print(al_reves)

