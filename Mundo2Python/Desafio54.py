#Meu jeito, minimamente errado mas no caminho certo

np = 0
anoAT = 2023

for c in range(1, 8):
    np += 1
    print(f"em que ano a {np} pessoa nasceu? " )
    anoNasc = int(input())
    idade = anoAT- anoNasc
    if idade >= 18:
        print(f"existem {c} pessoas maiores de idade")
    else :
        print(f"existem {c} pessoas menores de idade") 
    
    
    
    
#jeito do lorde guanabara 
    
from datetime import date 
    
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
        nasc= int(input(f"em que ano a {pess} pessoa nasceu? "))
        idade = atual - nasc 
        if idade >= 18:
            totmaior+= 1
        else:
            totmenor += 1
    
print(f"ao todo tiveram {totmaior} pessoas maiores e {totmenor} de pessoas menores! ")

    
    