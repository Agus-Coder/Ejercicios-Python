cadena = input("Ingrese algo con mas de 5 caracteres ")

cadena2 = input("Ingrese algo con mas de 5 caracteres ")

result = cadena.find(cadena2)

if result != -1:

    print(cadena2 + " es una subcadena de " + cadena)

