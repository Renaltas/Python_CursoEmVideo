# resolução do guanabara 
maior = 0
menor = 0 
for p in range(1,6):
    peso = float(input("insira o seu peso!: "))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print(f" o peso maior e o menor são {maior} e {menor}")   