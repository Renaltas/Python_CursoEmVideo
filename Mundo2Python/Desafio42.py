print('insira tres lados de um triangulo: ')
lado1 = int(input())
lado2 = int(input())
lado3 = int(input())

if lado1 == lado2 and lado1 == lado3:
    print('triangulo equilatero... ')
elif lado1 == lado2 and lado1 != lado3:
    print('triangulo isoceles... ')
elif lado1 != lado2 and lado1 != lado3:
    print('triangulo escaleno...')
else :
    print('não é triangulo')