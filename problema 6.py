""" Să se calculeze sumele:  s1=1+2+3+...+n
                             s2=1*2+2*3+3*4+...+(n-1)*n
                             s3=1+1*2+1*2*3+...+1*2*3*...*n
                             s4=12+22+32+...+n2
                             s5=1/2+2/3+3/4+...+n/(n+1)
                             s6=1+2+22+23+24+...+2n."""
a=int(input("dati un numar:"))
s1=0
for i in range(1,a+1):
    s1+=i
    print("s1=",s1)

a=int(input("dati un numar:"))
s2=0
for i in range(1,a+1):
    s2+=(i-1)*i
    print("s2=",s2)

a=int(input("dati un numar:"))
s3=1
pr=1
for i in range(2,a+1):
    pr*=i
    s3+=pr
    print("s3=",s3)

a=int(input("dati un numar:"))
s4=0
for i in range(1,a+1):
    s4+=(10*i+2)
    print("s4=",s4)

a=int(input("dati un numar:"))
s5=0
for i in range(1,a+1):
    s5+=a/(a+1)
    print("s5=",s5)

a=int(input("dati un numar:"))
s6=3
for i in range (2,n+1):
    n=str(i)
    s6+=int(str('2'+n))
    print("s6",s6)