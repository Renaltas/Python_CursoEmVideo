from  random import randint 
'''meu jeito!!!!'''
n = int(input("insira um numero entre 0 e 5: "))
if n > 0 and n < 5:
    if n == 3:
        print("vc acertou o numero parabens!!!!")
    else :
        print("vc errou o numero!!!!!!!")
else: 
    print("voce errou o numero!!!!!!")
    print("numero invalido não esta entre 0 e 5!!!!!")
    
    
    
''' jeito guanabara:'''
computador = randint(0, 5)
print("estou pensando em um numero entre 0 e 5 tente adivinhar")
jogador = int(input)
if jogador == computador:
    print("parabens vc venceu ")
else :
    print("vc perdeu ")