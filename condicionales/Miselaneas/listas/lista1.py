def seriefibo(numero):
    fibo=[]
    a,b=0,1
    while numero>0:
        fibo.append(a)
        a,b=b,a+b
        numero=numero-1
        print (fibo)
    
t=seriefibo(numero=int(input("ingrese el numero:")))

