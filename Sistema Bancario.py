from time import sleep
depositos, saques, movimentos, saldo, SaquesDiarios, LimiteSaque, entradas, saidas = [], [], [], 0, 3, 500, 0, 0
menu = 'p'

def opcoes():
    opcao = str(input('''
********** MENU PRINCIPAL **********
            
[ e ] Extrato de Transações
[ d ] Depósito
[ s ] Saque
[ c ] Sobre sua Conta
[ x ] Fechar o sistema

Digite a opção desejada => '''))
    return opcao

while menu != 'x':
    # Exibe as opções disponíveis
    menu = opcoes()

    # Depositar dinheiro
    if menu == 'd':
        Depositar_Valor = 0
        while True:
            Depositar_Valor = float(input('''
********** DEPOSITAR **********

Utilize esta opção para inserir
dinheiro em sua conta.
                                          
Para voltar ao menu principal
        digite 0
                                     
Digite o valor a ser depositado: R$ '''))
            if Depositar_Valor > 0:
                print(f'\n\nProcessando depósito no valor de R${Depositar_Valor:.2f}...')
                depositos.append(Depositar_Valor)
                saldo += Depositar_Valor
                movimentos.append('Depósito')
                movimentos.append(Depositar_Valor)
                entradas += Depositar_Valor
                sleep(2)
                print('\nDepósito confirmado!\nO valor já está disponível em sua conta.\nAcesse o Extrato para mais informações.')
                sleep(2)
            else:
                print('Retornando ao menu principal...')
                sleep(2)
            break

    # Sacar dinheiro
    elif menu == 's':
        Sacar_Valor = 0
        while True:
            Sacar_Valor = float(input(f'''
********** SACAR **********

Utilize esta opção para retirar
dinheiro de sua conta.
                                          
Para voltar ao menu principal
        digite 0
                                      
Saldo atual: R$ {saldo:.2f}
                                     
Digite o valor a ser retirado: R$ '''))
            if Sacar_Valor > 0:
                print(f'\n\nProcessando saque no valor de R${Sacar_Valor:.2f}...')
                if len(saques) <= SaquesDiarios:
                    sleep(1)
                    if Sacar_Valor <= LimiteSaque:
                        sleep(1)
                        if Sacar_Valor <= saldo:
                            saques.append(Sacar_Valor)
                            saldo -= Sacar_Valor
                            movimentos.append('Saque')
                            movimentos.append(Sacar_Valor)
                            print('\nSaque confirmado!\nAcesse o Extrato para mais informações.')
                            sleep(2)
                            saidas += Sacar_Valor
                        else:
                            print(f'\nSaldo insuficiente para realizar o saque de R$ {Sacar_Valor:.2f}')
                    else:
                        print('\nVocê está tentando sacar um valor maior que o permitido para sua conta.')
                else:
                    print('\nVocê atingiu o limite de saques diários permitidos para sua conta.')


            else:
                print('Retornando ao menu principal...')
                sleep(2)
            break

    # Extrato de movimentações
    elif menu == 'e':
        print('''
************ EXTRATO ************

Todas as movimentações de entrada e
saída da sua conta aparecem aqui.

''')
        sleep(1)
        # Checa se há movimentações na conta para exibir
        if len(movimentos) > 0:

            # Listar as movimentações Dep/Saq
            for m in range(1,len(movimentos),2):
                if movimentos[m-1] == 'Depósito': print(f'{movimentos[m-1]}: {movimentos[m]:.2f}+')
                else: print(f'{movimentos[m-1]}: {movimentos[m]:.2f}-')

            print(f'''\nSaldo atual: R$ {saldo:.2f}

Fim do extrato.

''')
            sleep(2)

        else:
            print('\nNão houve movimentação.')
            print('''

Fim do extrato.

''')
            sleep(2)

    # Dados da Conta
    elif menu == 'c':
        print(f'''
********** MINHA CONTA **********

Sua conta está ATIVADA!
              
Operações realizadas na data de hoje
Depósitos: {len(depositos)}
Saques: {len(saques)} de {SaquesDiarios}

Saldo atual: R$ {saldo:.2f}

Balanço:
Entradas R$ {entradas:.2f} x R$ {saidas:.2f} Saídas

Lembre-se que sua conta tem limite de
R${LimiteSaque} por saque. Valores acima disso
não serão aceitos pelo sistema do banco.''')
        if len(saques) >= SaquesDiarios: print('Você já atingiu seu limite diário de saques.\n\n\n')
        sleep(5)

    # Encerrar o sistema
    elif menu == 'x':
        print('\nObrigado por utilizar nossos serviços.\nSeu acesso foi encerrado. Até a próxima!\n')

    # Nenhuma das opções válidas
    else:
        print('Não foi digitada uma opção válida! Tente novamente.\n')
