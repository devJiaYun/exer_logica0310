# 5
n = int (input("Digite um número inteiro:"))

def primo(n):
    if n <= 1:
        return False  
    for i in range(2,n,+ 1):  
        if n % i == 0:  
            return False
    return True 

print(primo(n))   
  