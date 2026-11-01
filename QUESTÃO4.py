#SISTEMA DE EMPRÉSTIMO

nome = "Olá, Colaborador(a)! "
print(nome)
idade = int(input("Digite sua idade: "))
salario = float(input("Qual o seu salário atual? ").replace(",", "."))
tempo = int(input("Qual é o seu tempo trabalhado, em anos? "))
valor = float(input("Qual o valor solicitado? ").replace(",", "."))

if idade < 18:
    print("EMPRESTIMO NÃO PERMITIDO. ")

elif salario < 1500.00:
    print(f"Salário: R$ {salario:.2f}")("RENDA INSUFICIENTE. ")

elif tempo < 1:
    print("TEMPO DE TRABALHO INSUFICIENTE. ")

elif valor > salario*10:
    print("VALOR SOLICITADO MUITO ALTO. ")

else:
    print("UHUUUL! \nEMPRÉSTIMO PRÉ-APROVADO.")