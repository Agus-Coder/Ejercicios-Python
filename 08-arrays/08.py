a = [23, 67, 78, 101, 15, 1, 10, 7, 13, 27,5, 50, 1000, 100, 25, 20, 50 ]

max = 0
pmax = 0
min = 0
pmin = 0
long = len(a)

for i in range(0, long):
    if (i == 0 or a[i] > max and a[i] % 10 == 0):
        max = a[i]
        pmax = i
    if (i == 0 or (a[i] < min and a[i] % 5 == 0)):
        min = a[i]
        pmin = i

print("Max es %d en posicion %d y min es %d en posicion %d" %(max,pmax,min,pmin))