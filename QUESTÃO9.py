#QUESTÃO 9 - MAIOR E MENOR VALOR

quantidade = int(input("Quantos números você deseja informar? "))

maior = 0
menor = 0

for i in range(quantidade):

    numero = int(input(f"Digite o {i + 1}º número: "))

    if i == 0:
        maior = numero
        menor = numero

    else:
        if numero > maior:
            maior = numero

        if numero < menor:
            menor = numero

diferenca = maior - menor


print("          RESULTADO FINAL           ")


print("Maior número:", maior)
print("Menor número:", menor)
print("Diferença:", diferenca)
