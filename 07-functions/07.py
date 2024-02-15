def divisors(n):
    total = 0
    for i in range(1,n):
        if n % i == 0:
            total +=i
    return total

def perfecto(n):
    sum_divs = divisors(n)
    return sum_divs == n

def programa():
    number = int(input(f"Ingrese un numero para saber si es perfecto:\n"))
    result = perfecto(number)
    if result:
        print(f"{number} es un numero perfecto")
    else:
        print(f"{number} no es un numero perfecto")

programa()