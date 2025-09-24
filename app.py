menu = """
           BANCO
Escolha a operação desejada:

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: R$ "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!\n")
        else:
            print("Operação falhou! Valor inválido.\n")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: R$ "))
        saldo_insuficiente = valor > saldo
        acima_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if saldo_insuficiente:
            print("Operação falhou! Saldo insuficiente.\n")
        elif acima_limite:
            print("Operação falhou! O valor excede o limite permitido por saque.\n")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques atingido.\n")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!\n")
        else:
            print("Operação falhou! Valor inválido.\n")

    elif opcao == "3":
        print("\n         EXTRATO ")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("\n")

    elif opcao == "0":
        print("Tem certeza que deseja sair? Se sim pressione 1 para sair ou 0 se quiser continuar")
        if input() == "1":
            print("Obrigado por utilizar o nosso banco! Até a próxima.")
            break
        else:
            print("Operação cancelada. Voltando ao menu\n")

    else:
        print("Operação inválida! Por favor, selecione novamente.\n")
