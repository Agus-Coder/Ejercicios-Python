a = [23, 67, 78, 101, 15, 1, 10, 7, 13, 27 ]

max = 0
min = 0

long = len(a)

for i in range(0, long):
    if (i == 0 or a[i] > max):
        max = a[i]
    if (i == 0 or a[i] < min):
        max = a[i]

print("Max es %d y min es %d" %(max,min))