# 4
n = int (input("Digite um número inteiro positivo:"))

def fatorial (n):
    if n < 0:
        print("não e positivo")
    elif n == 0 or n == 1:
        print(n)
        return n
    else:
        resultado = 1
        for x in range(1, n + 1,+1):
            resultado *= x
        return resultado
        
print(fatorial (n))
