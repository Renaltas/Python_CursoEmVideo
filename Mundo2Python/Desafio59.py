v1 = int(input("insira o primeiro valor! "))
v2 = int(input("insira o segundo valor! "))
aT = int(input("insira os gotariua de fazer sendo que \n [1]Somar \n [2] multiplicar \n [3]maior \n [4] novos numeros \n2 [5]sair ")) # alternativa 

while aT != 5:
    if aT == 1:
        soma = v1 + v2
        print(f"a soma entre os numeros é de {soma}")
        aT = int(input("insira os gotariua de fazer sendo que \n [1]Somar \n [2] multiplicar \n [3]maior \n [4] novos numeros \n [5]sair\n"))
    elif aT == 2:
        multi = v1*v2
        print(f"a multiplicação entre eles é de {multi}")
        aT = int(input("insira os gotariua de fazer sendo que \n [1]Somar \n [2] multiplicar \n [3]maior \n [4] novos numeros \n2 [5]sair "))
    elif aT == 3:
        if v1 > v2:
            print(f"o maior numero é {v1}")
            aT = int(input("insira os gotariua de fazer sendo que \n [1]Somar \n [2] multiplicar \n [3]maior \n [4] novos numeros \n2 [5]sair "))
        elif v2 > v1:
            print(f"o maior numero é {v2}")
            aT = int(input("insira os gotariua de fazer sendo que \n [1]Somar \n [2] multiplicar \n [3]maior \n [4] novos numeros \n2 [5]sair "))
        elif v1 == v2:
            print("os numeros são iguais")
            aT = int(input("insira os gotariua de fazer sendo que \n [1]Somar \n [2] multiplicar \n [3]maior \n [4] novos numeros \n2 [5]sair "))
         
    elif aT == 4:
        print("gostaria de reescrever os numeros? ")
        v1 = int(input("insira o primeiro valor! "))
        v2 = int(input("insira o segundo valor! "))
        aT = int(input("insira os gotariua de fazer sendo que \n [1]Somar \n [2] multiplicar \n [3]maior \n [4] novos numeros \n2 [5]sair "))
    
    else: 
        print("numero invalido tente de novo")
        aT = int(input("insira os gotariua de fazer sendo que \n [1]Somar \n [2] multiplicar \n [3]maior \n [4] novos numeros \n2 [5]sair "))
        
    # de prima krl o pai é brabo, só quero passar na prova do Massa pelo amor 

    