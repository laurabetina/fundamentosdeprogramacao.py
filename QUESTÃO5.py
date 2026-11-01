#QUESTÃO 5 - MÉDIA DE VALORES

quantidade = int(input("Olá Usuaria(o)! Quantos números serão informados? "))

soma = 0

for i in range(1, quantidade + 1):
    valor = float(input("Digite o " + str(i) + "º valor: "))

    soma += valor

    if i == 1:
        maior = valor
        menor = valor
    else:
        if valor > maior:
            maior = valor

        if valor < menor:
            menor = valor

media = soma / quantidade

print("Soma dos valores:", soma)
print("Média dos valores:", media)
print("Maior valor:", maior)
print("Menor valor:", menor)