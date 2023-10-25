valor = float(input("insira o valor a ser pago: "))
formaP = int(input("insira a forma de pagamento: "))
print("a vista dinheiro/cheque[1]")
print("a vista no cartão [2]")
print("2x no cartão [3]")
print("3x no cartão [4]")


if formaP ==1:
    novoP = valor - (valor*0.1)
    print(f"sua compra de {valor} vai custar {novoP}") 
elif formaP ==2:
    novoP = valor-(valor*0.05)
    print(f"sua compra de {valor} vai custar {novoP}") 
elif formaP ==3:
    parcela = valor/2
    novoP = valor
    print(f"a sua parcela sera de {parcela}")
    print(f"sua compra de {valor} vai custar {novoP}") 
elif formaP ==4:
    novoP = valor +(valor*0.2)
    print(f"sua compra de {valor} vai custar {novoP}") 
else:
    print("opção de pagamento invalido!!!")
    