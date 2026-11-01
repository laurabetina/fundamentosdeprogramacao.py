#QUESTÃO 2 - NÚMEROS PARES

nome = int(input("Olá Usuário(a)\nDigite um número inteiro positivo: "))
quantidade = 0

print("NÚMEROS PARES")

for i in range (1, nome + 1): 
    if i % 2 == 0:
     print(i)
     quantidade += 1

print("Quantidade números pares: ", quantidade)
