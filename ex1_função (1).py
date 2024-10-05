# 1
# import math

# a = float(input("Digite o valor A: "))
# b = float(input("Digite o valor B: "))
# c = float(input("Digite o valor C: "))

# def equação (a,b,c):
#     delta = (b**2-4*a*c)
#     if delta > 0:
#         x1= (-b - math.sqrt(delta))/(2*a)
#         x2= (+b - math.sqrt(delta))/(2*a)
#         print ("As raizes são:", x1, x2)
#         return x1,x2
#     elif delta == 0:
#         x = (-b)/(2*a)
#         print ("A raiz é :", x) 
#         return x
#     else:
#         return"A equação não tem raizes reais"          
# equação(a,b,c)


#2
# a = float(input("Digite um valor A: "))
# b = float(input("Digite o valor B: "))
# def soma (a,b):
#     s = a+b
#     print (s)
#     return s

# soma (a,b)


# 3
# a = float(input("Digite um valor A: "))
# def pares (a):
#     if a % 2 ==0:
#         print ("True")
#         return a
#     else:
#         print("False")
#         return a

# pares(a)


# 4
# n = int (input("Digite um número inteiro positivo:"))
# if n < 0:
#     print("não e positivo")
# else:
#     def fatorial (n):
#         return n * fatorial(n-1)

# fatorial (n)

5
n = int (input("Digite um número inteiro:"))

def primo (n):
    if n < 2