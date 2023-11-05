somaIdade = 0 
mediaIdade = 0
maiorIdadeHomem = 0 
nomeVelho= ''
totmulher20 = 0
 
for c in  range(1,5):
    print(f"{c} Pessoa")
    nome = input("insira seu nome: ")
    idade = int(input("insira a sua idade: "))
    sexo = str(input("insira o seu sexo: "))
    somaIdade += 1
    if c == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if  sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > 20:
        totmulher20 += 1
        
media = somaIdade/4
print(f"a media da idade é de: {media} ")
print(f"o homem mais velho é de: {nomeVelho} ")
print(f"ao todo são {totmulher20} mulheres menores qeu 20 anos")

#jesus que baguio gigante da porra  
 
    
    
