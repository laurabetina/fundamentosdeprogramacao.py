#QUESTÃO 7 - CONTAGEM DE NÚMEROS POSITIVOS E NEGATIVOS

print("Digite 10 números inteiros positivos ou negativos")
positivos = 0
zeros = 0
negativos = 0

for i in range (10):
    v = int(input(f"Digite o {i+1}º valor: "))
    
    if v > 0:
        positivos += 1
    if v == 0:
        zeros += 1
    if v < 0:
        negativos += 1

print(f"\nPositivos: {positivos}\nNegativos: {negativos}\nZeros: {zeros}")