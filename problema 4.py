"""Utilizând ciclul FOR elaborați un program care afișează toate numerele impare, pentru intervalul de la a la b (a și b se citesc de la tastatură)."""
a=int(input("dati un numar:"))
b=int(input("dati un numar:"))
for i in range(a,b):
    if i%2!=0:
        print(i)
    