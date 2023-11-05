sexo = str(input("insira o seu sexo [M/f]"))

while sexo != 'M' and sexo != 'm' and sexo != 'F' and sexo != 'f':  # while sexo not in 'MmFf' maneira mais facil de coisar o coiso 
    print("sexo invalido digite novamente!")
    sexo = str(input("insira o sexo [M/f]"))
    
if sexo == 'F' or sexo == 'f' :
    print("seu sexo é feminino!")
elif sexo == 'M' or sexo == 'm':
    print("seu sexo é masculino!")