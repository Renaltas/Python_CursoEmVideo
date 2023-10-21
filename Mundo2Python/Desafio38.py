n = int(input("digite o numero "))
n2 = int(input("digite outro numero "))

if n > n2:
    print(f"o maior numero é {n}")
elif n2 > n:
    print(f"o maior numero é {n2}")
elif n == n2 :
    print(f"os numero são iguais")
else :
    print("numero invalidos !")
    
