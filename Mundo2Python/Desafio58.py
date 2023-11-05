from random import randint

computador = randint(0,10)
tent = 0
jogador = int(input("insira a sua jogada e veremos se vc acertou"))
while jogador != computador:
    if computador > jogador:
        print("Mais ...tente outra vez!")
        jogador = int(input("insira a sua jogada e veremos se vc acertou"))
    elif jogador > computador:
        print("menos... tente outra vez")
    tent+= 1
    
print(f"Pabuais vc acertou e seu numero de tentativas foi de {tent}")

# de prima ta, o cara é pika tem nem oq fazer 

