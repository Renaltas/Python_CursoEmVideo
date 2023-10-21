print("insira tres lados de um triangulo")
lado1 = int(input())
lado2 = int(input())
lado3 = int(input())

if lado1 < lado2+lado3 and lado2 < lado1+lado3 and lado3< lado2+lado1:
    print("isso pode ser um triangulo!")
else :
    print("isso não pode ser um triangulo!")