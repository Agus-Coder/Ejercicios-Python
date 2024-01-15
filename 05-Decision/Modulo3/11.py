quantity = int(input("ingrese la cantidad de perfectos deseados"));

encontrados = 0
sumaDivs = 0
stop=2
# print("before while");

while not(encontrados==quantity):

    # print("encontrados: ", encontrados,"quantity: ", quantity);

    for i in range(1,int(stop/2 + 1)):
        if stop%i == 0:
            sumaDivs += i

    # print("suma divs: ", sumaDivs);
        
    if sumaDivs == stop:
        print("El numero perfecto, posicion: ", encontrados, " es ", stop)
        encontrados += 1
        print("Cantidad total encontrada: ", encontrados)
    
    sumaDivs = 0
    stop += 1
    # print("stop: ", stop,"encontrados: ", encontrados);
