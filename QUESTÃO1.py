# QUESTÃO 1 - CLASSIFICAÇÃO DE IDADE 

idade =  int(input("Olá, Usuário(a)!\nDigite sua idade: "))

if idade < 0:
    print ("IDADE INVÁLIDA")

elif idade <=12:
    print ("CRIANÇA")

elif idade <=17:
    print ("ADOLESCENTE")

elif idade <=59:
    print ("ADULTO")

else:
    print ("IDOSO")






