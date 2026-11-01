#Questão 10 - CAIXA ELETRONICO

saldo = 1000.0
opcao = 0

while opcao != 4:
    opcao = int(input("ESCOLHA UMA OPÇÃO A SEGUIR: \n1-Consultar Saldo\n2-Depositar Saldo\n3-Sacar Saldo\n4-Sair"))
    match opcao:
        case 1:
            print(f"\nSaldo atual: R${saldo:.2f}")
            
        case 2:
            deposito = float(input(f"\nDigite o valor do depósito: R$"))
            saldo += deposito
            
            print(f"Depósito realizado!\nSaldo atual: R${saldo:.2f}")
        
        case 3:
            saque = float(input(f"\nDigite o valor de saque: R$"))
            while saque > saldo:
                saque = float(input(f"Saque não autorizado. Saldo insuficiente para realizar esta operação.(R${saldo:.2f}).\nTente outro valor: R$"))

            saldo -= saque
            print(f"Saque realizado com sucesso!\nSaldo atual: R${saldo:.2f}")
        
        case 4:
            print("Sessão Finalizada!")
            break
        
        case _:
            print("\nOpção inválida. Tente novamente.")