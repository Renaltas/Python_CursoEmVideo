nota1 = float(input("insira a preimeira nota: "))
nota2 = float(input("insira a segunda nota: "))
media = (nota1+nota2)/2

if media < 5.0:
    print("aluno reprovado!!!")
    print(f"a media é {media}")
elif media > 5.0 and media < 6.9:
    print("recuperação!!!")
    print(f"a media é {media}")
elif media >= 7:
    print("aprovado!!!")
    print(f"a media é {media}")
    
