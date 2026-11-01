#QUESTÃO 8 - SISTEMA DE NOTAS


print("     BEM-VINDO(A), USUÁRIO(A)!     ")
print("       CADASTRO DE NOTAS            ")

aprovados = 0
recuperacao = 0
reprovados = 0
total = 0

nota = float(input("\nDigite a nota do estudante (-1 para encerrar o cadastro): "))

while nota != -1:

    if nota >= 7:
        print("ESTUDANTE APROVADO! ")
        aprovados += 1

    elif nota >= 5:
        print("ESTUDANTE EM RECUPERAÇÃO! ")
        recuperacao += 1

    else:
        print("ESTUDANTE REPROVADO! ")
        reprovados += 1

    total += 1

    nota = float(input("\nDigite a nota do próximo estudante (-1 para encerrar o cadastro): "))

print("          RESULTADO FINAL           ")

print("Quantidade de aprovados:", aprovados)
print("Quantidade em recuperação:", recuperacao)
print("Quantidade de reprovados:", reprovados)
print("Quantidade total de estudantes:", total)
