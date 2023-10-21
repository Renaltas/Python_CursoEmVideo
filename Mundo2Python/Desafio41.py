from datetime import date 
anoAT = date.today().year
anoN = int(input("insira o ano de nascimento: "))
idade = anoAT-anoN

if idade <= 9:
    print(f" o atleta tem {idade}")
    print("classificação : MIRIM")
elif idade <= 14:
    print(f" o atleta tem {idade}")
    print("classificação : INFANTIL")
elif idade <= 19:
    print(f" o atleta tem {idade}")
    print("classificação : JUNIOR")
elif idade <= 25:
    print(f" o atleta tem {idade}")
    print("classificação : SENIOR")
elif idade  > 25:
    print(f" o atleta tem {idade}")
    print("classificação : MASTER")

    

