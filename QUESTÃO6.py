#QUESTÃO 5 - VALIDAÇÃO DE SENHA

senha = "1234"

nome = (input("Bem-vindo(a), Usuário(a)!\nQual a senha? : "))

while nome != senha:
     nome = input("ACESSO NEGADO! Tente Novamente: ")

print("ACESSO AUTORIZADO! Bem-vindo(a)! ")