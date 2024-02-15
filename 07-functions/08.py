def prime_number(n):
    divisors = 0
    for i in range(1,n):
        if n % i == 0:
            divisors +=1
        if divisors >1:
            break
    return divisors < 2

def program():
    for i in range(100,201):
        is_prime = prime_number(i)
        if(is_prime):
            print(f"{i} es un  numero primo")

program()