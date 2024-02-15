a = [23, 1, 67, 78, 101, 15, 1, 10, 7, 13, 27, 1, 1, 700, 50, 24, 200, 40 ]
b = [ 12, 77, 60, 7, 13, 101, 40, 3, 2, 55, 200]

lenga = len(a)
lengb = len(b)
c = []

for i in range(0, lenga):
    for j in range(0, lengb):
        if(a[i] == b[j]):
            c.append(a[i])
            continue

print(c)