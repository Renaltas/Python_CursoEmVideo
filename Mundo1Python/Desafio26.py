frase = input("insira um frase: ").strip().upper()

print(f"a letra A aparace {frase.count('A')} vezes")
print(f"a prmeira letra a apareceu na posição: {frase.find('A')+1}")
print(f"a ultima letra a aparece na {frase.rfind('A')+1}")


