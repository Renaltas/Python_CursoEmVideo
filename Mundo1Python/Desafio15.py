km = float(input("insira a quilometragem reodada: "))
dias = int(input("insira a quantidade de dias rodados: "))
preDia= dias*60
prekm= km*0.15
preTotal = preDia+prekm
print(f"o preço total a se pagar é: {preTotal}")
