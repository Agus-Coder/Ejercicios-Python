def triple(n):
    result = 3*n
    return result

def siguiente(n):
    result = n+1
    return result

# el consecutivo del triple del numero

def programa():
    n = int(input("Ingrese un numero:\n"))
    trip = triple(n)
    sig = siguiente(n)
    sig_trip = siguiente(trip)
    trip_sig = triple(sig)

    print(f"El consecutivo del triple de {n} es {sig_trip}.\nEl triple del consecutivo de {n} es {trip_sig}")


programa()