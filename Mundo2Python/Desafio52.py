import time

n = int(input("insira um numero: "))
print("veremos se ele é primo ou não: ")
time.sleep(3)
tot = 0
for c in range(1,n+1,):
    if n % c == 0 :
       tot += 1 
   
print(f"o numero {n} foi divisivel {tot} vezes")
if tot == 2:
    print("esse numero é primo ")
else:
    print("esse numero não é primo ")