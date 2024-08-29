menu = """

[d] Deposito
[s] Sacar
[e] Extrato
[q] Sair


=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            
        else:
            print("Operação inválida!. Por favor, digite um valor válido.")
        
    elif opcao == "s":
        valor = float(input("Infomre o valor de saque: "))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Saldo insuficiente para saque!")
            
        elif excedeu_limite:
            print("Você excedeu o limite de saque!")
            
        elif excedeu_saques:
            print("Você excedeu o limite de saques!")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saques += 1
            
        else:
            print("Operação inválida!. Por favor, digite um valor válido.")
        
    elif opcao == "e":
        print("\n=============== EXTRATO ===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")
        
    elif opcao == "q":
        break
    
    else:
        print("Opção invalida, por favor selecione novamente a operação desejada.")