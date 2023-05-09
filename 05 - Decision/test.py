cont = 0
cont1 = 0
edad = int(input("ingrese edad"))
while(edad>0):
    cont1+=1
    if(edad>18):
        cont+=1
if(cont!=0):
    print('el proncetaje de mayores es ', cont*100/cont1 )