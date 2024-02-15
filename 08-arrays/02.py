a = [1,2,3,4,5,6,7,8,9,10]

print(a[3])

lenght = len(a)

c = []

for i in range (lenght,0,-1):
    c.append(i)
print(c)

print(a[0]*a[lenght-1])

ac = 0
mul = 1
for i in range (0,lenght,1):
    if i % 2 != 0:
        print(i)
        mul *= i
    if i % 2 == 0:
        ac += i
    
print(ac)
print(mul)

b = a[lenght-1]
a[lenght-1] = a[0]
a[0] = b

print(a)
