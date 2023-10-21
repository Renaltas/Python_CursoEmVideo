velo = float(input("insira  a sua velocidade para ver a sua multa::"))
multa = (velo-80)*7
if velo > 80:
    print("vc foi multado!!!!! ")
    print(f"e o valor da multa é de {multa}")
else:
    print("vc é um otimo motorista :>")