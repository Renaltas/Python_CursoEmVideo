anoN = int(input("insira seu ano de nascimento: "))
anoAt = int(input("insira o ano atual: "))
anoAL = anoN+18
idade = anoAt-anoN

if idade > 18:
    print(f"vc tem {idade} anos e ja deveria ter se alistado em {anoAL} ")
    fOs = anoAt - anoAL
    print(f"vc deveria ter se alistado há {fOs}anos")
elif idade < 18:
    print("vc ainda não deve se alistar!!")
    print(f"vc tem {idade} anos  e deve se alistar somente em {anoAL}")
    fOs = anoAL-anoAt
    print(f"vc deve se alistar em {fOs} anos")
elif idade == 18:
    print(f"vc esta com {idade} anos e ja pode se alistar nesse ano que é {anoAL}")
    


