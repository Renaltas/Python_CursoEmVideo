n = int(input("digite um numero inteiro: "))
print("escolha uma das bases para conversão: ")
print("[1] converter apra binario: ")
print("[2] converter para octal: ")
print("[3] converter para hexadecimal: ")
nD = int(input())
if nD == 1:
    n = bin(n)
    print(f"a conversão é {n}")
elif nD == 2:
    n = oct(n)
    print(f"a conversão é {n}")
elif nD == 3:
    n = hex(n)
    print(f"a conversão é {n}")
else :
    print("esse numero não está no catálogo")
    
