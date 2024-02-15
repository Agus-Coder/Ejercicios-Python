a = [23, 1, 67, 78, 101, 15, 1, 10, 7, 13, 27, 1, 1, 700, 50, 24, 200, 40 ]

min = 0

places = []

long = len(a)

for i in range(0, long):
    if (i == 0 or a[i] < min):
        min = a[i]

for i in range(0, long):
    if (a[i] == min):
        places.append(i)

print(places)