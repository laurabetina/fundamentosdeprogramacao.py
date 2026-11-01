#QUESTÃO 4 - TABUADA

numero = int(input("Olá Usuário(a)! \nDigite um número: "))

for i in range(1, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)