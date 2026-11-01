#MENU DE SISTEMA

print("    **MENU DO SISTEMA**   ")
print("1. CADASTRAR ALUNO")
print("2. CONSULTAR ALUNO")
print("3. ALTERAR ALUNO")
print("4. EXCLUIR ALUNO")
print("5. LISTAR ALUNOS")
print("6. SAIR")

opcao = int(input("Digite um número de 1 à 5 ou digite 6 para SAIR: "))

match opcao:
    case 1:
        print("Você selecionou a opção 1 - CADASTRAR ALUNO! ")

    case 2: 
        print("Você selecionou a opção 2 - CONSULTAR ALUNO! ")

    case 3:
        print("Você selecionou a opção 3 - ALTERAR ALUNO! ")

    case 4:
        print("Você selecionou a opção 4 - EXCLUIR ALUNO! ")

    case 5:
        print("Você selecionou a opção 5 - LISTAR ALUNOS! ")

    case 6:
        print("Você selecionou a opção 6 - SAIR!\nSistema encerrado.")

    case _ :
        print("OPÇÃO INVÁLIDA")

    