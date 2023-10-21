casa = float(input("insira o valor da casa: "))
sal = float(input("insira o valor do seu salario: "))
quantAnos = int(input("em quantos anos vc pretende pagar?: "))
parcela = casa/(quantAnos*12)


if parcela > sal*0.3:
    print("emprestimo negado")
elif parcela < sal*0.3:
    print("emrprestimo aceito")

    