peso = float(input("insira o seu peso: "))
altura = float(input("insira o sua altura: "))

imc = peso/(altura**2)

if imc < 18.5 :
    print("abaixo do peso!")
    print(f"o seu imc é de {imc}")
elif imc > 18.5  and imc < 25:
    print("peso ideal!")
    print(f"o seu imc é de {imc}")
elif imc > 25 and imc < 30:
    print("sobrepeso ")
    print(f"o seu imc é de {imc}")
elif imc > 30 and imc < 40:
    print("obesidade")
    print(f"o seu imc é de {imc}")
elif imc > 40:
    print("obesidade morbida")
    print(f"o seu imc é de {imc}")
    
