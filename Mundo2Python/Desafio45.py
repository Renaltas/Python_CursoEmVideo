from random import randint
intens = ( 'pedra', 'papel' , 'tesoura')
computador = randint(0,2)
print(" suas opções[0] pedra [1] papel [2]tesoura ")
jogador = int(input("qual é a sua jogada? "))
print(f"jogador escolheu {jogador}")
print(f" o computador escolheu {computador}")

if computador == 0:
    if jogador == 0:
        print("empate!")
    elif jogador == 1:
        print("jogador vence!")
    elif jogador == 2:
        print("computador vence!")
    else:
        print("jogada invalida!")

elif computador == 1:
    if jogador == 0:
        print("computador vence!")
    elif jogador == 1:
        print("empate")
    elif jogador ==2:
        print("jogador vence!")
    else:
        print("jogada invalida!")
        
elif computador == 2:
    if jogador ==0:
        print("jogador vence!")
    elif jogador == 1:
        print("computador vence!")
    elif jogador == 2:
        print("empate")
    else:
        print("jogada invalida!")
        
