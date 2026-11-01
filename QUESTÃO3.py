#ELEGIBILIDADE PARA BOLSAS

nome = "Olá, Usuário(a)! "
print(nome)
media = float(input("Digite sua média acadêmica: ").replace(",", "."))
percentual = float(input("Qual o seu percentual de frequêncial? ").replace("%", "").replace(",", "."))
renda = int(input("Qual a sua Renda Familiar em R$ (sua renda + a dos integrantes das pessoas que moram com você)? "))
bolsa = input("Você possui alguma outra bolsa (responda com sim ou não.)? ").upper()

if media < 7: 
    print("Aluno INELEGÍVEL \nMotivo: Média insuficiente")


elif percentual < 75:
    print("Aluno INELEGÍVEL \nMotivo: Percentual de frequência INSUFICIENTE")

elif renda > 3000:
    print("Aluno INELEGÍVEL \nMotivo: renda familiar acima do limite! ")

elif bolsa == "sim":
    print("Aluno INELEGÍVEL \nMotivo: O aluno(a) já possui outra bolsa. ")

else:
     print("ALUNO ELEGÍVEL")


