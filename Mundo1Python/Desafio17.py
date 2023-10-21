import math

cat1 = float(input("insira o cateto: "))
cat2 = float(input("insira outro cateto: "))

hip = math.sqrt(cat1**2 + cat2**2)
print(f"a hipotenusa é: {hip}")
