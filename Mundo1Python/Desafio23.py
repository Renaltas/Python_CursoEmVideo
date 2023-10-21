num = int(input("insira o seu numero: "))
u = num //1 % 10 
d = num //10 % 10
c = num //100 % 10
m = num //1000 %10
print(f"a unidade é: {u}")
print(f"a dezena é: {d}")
print(f"a centena é: {c}")
print(f"o milhar é: {m}")
