
#Meu jeito 
#Não ultilizei for, pq não sabia como colocar nessa situaçãoxe acabpu que nem precisou :O
#guanabara ensinou esse macete dps que eu fiz
f = input("digite uma frase;")
print("vamos ver se ela é um palindrome:  ")

fI = f[::-1]
if fI == f:
    print("é um palindrome! ")
    print(f"o inverso da frase {f} é {fI}")
else:
    print("não é um palindrome! ")
    print(f"o inverso da frase {f} é {fI}")
          
print("fim da bagaça")

#Jeito do guanabara 
#maldito exercicio, abalou psicologico 

frase = input("insira um frase: ").strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
if inverso == junto:
    print("temos um palindromo ")
else: 
    print("não temos um palindromo")

