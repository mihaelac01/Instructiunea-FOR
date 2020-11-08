"""Utilizând ciclul FOR elaborați un program care să calculeze suma numerelor de la 1 la n, care se împart la 3 și 5 pentru oricare n introdus de la tastatură."""
a=int(input("dati un numar:"))
s=0
for i in range(1,a):
    if (i%3==0)and(i%5==0):
        s+=i
        print("suma este =",s)