# 1
import math

a = float(input("Digite o valor A: "))
b = float(input("Digite o valor B: "))
c = float(input("Digite o valor C: "))

def equação (a,b,c):
    delta = (b**2-4*a*c)
    if delta > 0:
        x1= (-b - math.sqrt(delta))/(2*a)
        x2= (+b - math.sqrt(delta))/(2*a)
        print ("As raizes são:", x1, x2)
        return x1,x2
    elif delta == 0:
        x = (-b)/(2*a)
        print ("A raiz é :", x) 
        return x
    else:
        return"A equação não tem raizes reais"          
equação(a,b,c)


