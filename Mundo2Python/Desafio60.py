n = int(input("digite um numero para calcular seu fatorial! "))
c = n 
f = 1
print("Calculando...")
while c > 0 :
    print(c , end = '')
    print(' x ' if c > 1 else ' = ', end = '')
    f *= c
    c -= 1
    
print(f)

#Refazer esse exercio 