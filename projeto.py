import random  # Importação de biblioteca de números aleatórios
import getpass  # Importação de biblioteca de senha oculta
import os  # Importação para o usuário digitar qualquer tecla e voltar ao menu

# Variáveis globais para usar em funções
limite_credito = 0
valor_deposito = 0
saque = 0
nome = ''
numeros_conta = random.randint(1000, 9999)  # Criando uma lista e gerando números aleatórios de 4 dígitos
senha_digitada = ''
historico_operacoes = []  # Criação de lista para armazenar os dados
saldo_total = 0
saldo_total_cofre = 0

print('MACK BANK - ESCOLHA UMA OPÇÃO')

def escolha_opcoes():  # Função para a escolha de opção do usuário
    print('(1) CADASTRAR CONTA CORRENTE')
    print('(2) DEPOSITAR')
    print('(3) SACAR')
    print('(4) CONSULTAR SALDO')
    print('(5) CONSULTAR EXTRATO')
    print('(6) COFRE DIGITAL')  # Criação de nova opção do menu
    print('(7) FINALIZAR')
    escolha = int(input('Digite a opção: '))  # input da escolha
    while escolha < 1 or escolha > 7:  # Verificando se o número digitado é válido, se não for, irá pedir até ser
        print(f'Opção inválida. Você digitou um número inexistente ({escolha})!')
        escolha = int(input('Digite novamente sua opção (1 - 7): '))
    return escolha

def solicitar_nome():  # Função para solicitar o nome
    nome_digitado = input('NOME DO CLIENTE: ')  # Input do nome
    return nome_digitado

def solicitar_senha():  # Função para solicitar a senha
    senha_digitada = getpass.getpass('SENHA (COM 6 CARACTERES): ')  # Input da senha com caracteres ocultos (getpass)
    while len(senha_digitada) != 6:  # Entrando em um loop caso a senha possua menos que 6 caracteres
        print(f'SENHA INVÁLIDA - sua senha possui {len(senha_digitada)} caracteres!')  # Mostrando o erro cometido
        senha_digitada = getpass.getpass('Por favor, digite uma senha com 6 caracteres: ')  # Pedindo o input novamente
    return senha_digitada

def repetir_senha(senha):  # Função para repetir a senha
    senha_repetida_digitada = getpass.getpass('REPITA A SENHA: ')  # Confirmação da senha já digitada
    while senha_repetida_digitada != senha:  # Entrando em um loop caso a senha seja diferente da já digitada
        print('Senha inválida. Sua senha digitada está diferente da senha já digitada!')  # Exibindo a mensagem do erro
        senha_repetida_digitada = getpass.getpass('Por favor, REPITA A SENHA: ')  # Input da mesma senha já digitada
    return senha_repetida_digitada

def cadastro_conta():  # Função caso o usuário digite 1 (tela de cadastro)
    global saldo_total  # Usando a variável global para o saldo inicial
    global nome  # Usando a variável global para o nome
    global senha_digitada  # Usando variável global para a senha que o usuário digitou
    global historico_operacoes  # Definindo a variável historico_operacoes como global
    global limite_credito  # Usando a variável global para limite_credito

    print('------------------------------------------------------------')
    print('MACK BANK – CADASTRO DE CONTA')
    print(f'NÚMERO DA CONTA: {numeros_conta}')  # Print do número da conta (números aleatórios)
    nome = solicitar_nome()  # Input do nome
    telefone = input('TELEFONE: ')  # Input do telefone
    email = input('EMAIL: ')  # Input do email
    saldo_inicial = float(input('SALDO INICIAL: R$ '))  # Input do saldo inicial

    while saldo_inicial < 1000:  # Entrando em um loop caso o saldo seja menor que R$ 1000,00
        print(f'Saldo inválido. O saldo digitado foi R$ {saldo_inicial:.2f}')  # Exibindo a mensagem do erro
        saldo_inicial = float(input('Por favor, digite um SALDO INICIAL maior que R$ 1.000,00: R$ '))  # Pedindo novamente o input

    saldo_total = saldo_inicial  # Garantindo que o saldo total seja o mesmo que o inicial para operações futuras
    limite_credito = float(input('LIMITE DE CRÉDITO: R$ '))  # Input do limite de crédito

    while limite_credito <= 0:  # Entrando em loop caso o limite de crédito seja menor que 0
        print(f'Limite de crédito NEGADO! Seu limite de crédito digitado foi R$ {limite_credito:.2f}')  # Mostrando a mensagem do erro
        limite_credito = float(input('Digite o limite de crédito (maior que R$ 0,00): '))  # Input novamente

    if limite_credito > 0:  # Verificando se limite de crédito é maior que 0
        print(f'LIMITE DE CRÉDITO: R$ {limite_credito:.2f}')  # Mostra o limite de crédito digitado

    senha_digitada = solicitar_senha()  # Usando a função para solicitar a senha e armazenando na senha_digitada
    repetir_senha(senha_digitada)  # Usando a função para repetir a senha e passando a senha original para comparação

    print('CADASTRO REALIZADO!')
    os.system('pause')  # Voltando para a tela inicial

    historico_operacoes.append(f"Cadastro realizado com saldo inicial de R$ {saldo_inicial:.2f}")  # Acrescentando na lista os dados de saldo inicial

    return limite_credito  # Armazenando valor de limite de crédito

def depositar():
    global nome  # Usando a variável global nome para exibir o nome digitado pelo usuário
    global saldo_total  # Usando a variável global para exibir o saldo total
    global historico_operacoes  # Usando a variável global para o histórico de operações

    print('------------------------------------------------------------')
    print('MACK BANK - DEPÓSITO EM CONTA')
    numero_conta = int(input('INFORME O NÚMERO DA CONTA: '))  # Input do número da conta já registrado

    while numero_conta != numeros_conta:  # Verificando se o número da conta digitado é diferente ao número registrado
        print('Seu número de conta digitado é INVÁLIDO.')
        numero_conta = int(input('INFORME O NÚMERO DA CONTA JÁ CADASTRADO: '))  # Caso não seja, input novamente

    if numero_conta == numeros_conta:  # Verificando se o número da conta digitado é igual ao número registrado
        print(f'NOME DO CLIENTE: {nome.title()}')  # Exibindo o nome com letras maiúsculas nas primeiras letras
        valor_deposito = float(input('VALOR DO DEPÓSITO: R$ '))  # Input do valor do depósito

        while valor_deposito <= 0:  # Verificando se o valor digitado é maior que 0, caso não, pedindo o input novamente
            print('O valor do depósito digitado é INVÁLIDO! Digite um depósito maior que R$ 0,00.')
            valor_deposito = float(input('VALOR DO DEPÓSITO: R$ '))  # Input novamente

        saldo_total += valor_deposito  # Somando e atualizando o saldo total com o valor do depósito

        print(f'DEPÓSITO REALIZADO COM SUCESSO! Saldo atual: R$ {saldo_total:.2f}')  # Exibindo o saldo total
        os.system('pause')  # Voltando para a tela inicial

        historico_operacoes.append(f"DEPÓSITO: R$ {valor_deposito:.2f}. SALDO TOTAL: R$ {saldo_total:.2f}")  # Acrescentando na lista os dados do valor do depósito e do saldo total

def sacar():
    global senha_digitada  # Usando variável global para a senha que o usuário digitou
    global saldo_total  # Usando a variável global para exibir o saldo total
    global historico_operacoes  # Usando a variável global para o histórico de operações
    global limite_credito  # Usando a variável global para limite_credito

    cont = 3  # Inicializando o contador

    print('------------------------------------------------------------')
    print('MACK BANK – SAQUE DA CONTA')
    numero_conta = int(input('INFORME O NÚMERO DA CONTA: '))  # Solicitando o número da conta

    while numero_conta != numeros_conta:  # Verificando caso o número não seja igual ao já registrado será pedido até ser o mesmo
        print('Seu número de conta digitado é INVÁLIDO.')
        numero_conta = int(input('INFORME O NÚMERO DA CONTA JÁ CADASTRADO: '))  # Input novamente

    if numero_conta == numeros_conta:  # Verificando se o número da conta é igual ao número registrado
        senha = getpass.getpass('DIGITE A SENHA: ')  # Solicitando a senha de 6 caracteres com a biblioteca getpass

        while senha != senha_digitada:  # Caso a senha seja diferente da registrada, entrará no while
            cont -= 1  # Contador diminui 1 a cada vez que a senha for errada
            if cont > 0:
                print(f'SENHA INVÁLIDA! Você tem mais {cont} tentativa(s).')
                senha = getpass.getpass('Por favor, digite a senha correta: ')  # Pedindo o input da senha novamente
            else:  # Se o contador for igual a 0, não há mais tentativas e volta para a tela inicial
                print('Você excedeu o limite de tentativas permitidas (3 tentativas).')
                os.system('pause')  # Voltando para a tela inicial
                return

        if senha == senha_digitada:  # Verificando se a senha é igual à senha digitada e registrada
            saque = float(input('QUAL O VALOR DO SAQUE? R$ '))  # Input do valor do saque

            while saque > saldo_total + limite_credito:  # Entrando em loop caso o saque seja maior que o saldo total e o limite de crédito
                print(f'Valor do saque (R$ {saque:.2f}) maior que o saldo total + limite de crédito (R$ {saldo_total + limite_credito:.2f})!')
                print('Por favor, digite um valor menor!')
                saque = float(input('QUAL O VALOR DO SAQUE? R$ '))  # Input do valor do saque novamente

            if saque <= saldo_total + limite_credito:  # Verificando se o valor do saque é menor ou igual ao saldo total + limite de crédito
                saldo_total -= saque  # Atualizando o saldo total

                print(f'SAQUE REALIZADO COM SUCESSO! Saldo atual: R$ {saldo_total:.2f}')  # Exibindo o saldo total
                os.system('pause')  # Voltando para a tela inicial

                historico_operacoes.append(f'SAQUE: R$ {saque:.2f}. SALDO TOTAL: R$ {saldo_total:.2f}')  # Acrescentando na lista os dados do valor do saque e do saldo total

def cofre_digital():
    global saldo_total  # Usando a variável global para exibir o saldo total
    global saldo_total_cofre  # Usando a variável global para o saldo total do cofre digital
    global historico_operacoes  # Usando a variável global para o histórico de operações

    print('------------------------------------------------------------')
    print('MACK BANK – COFRE DIGITAL')
    print('Neste momento você pode depositar o valor desejado no cofre digital, porém não poderá')
    print('retirar o valor depositado até 3 dias após o depósito.')

    valor_deposito_cofre = float(input('QUAL O VALOR DO DEPÓSITO? R$ '))  # Solicitando o valor do depósito no cofre digital

    while valor_deposito_cofre <= 0 or valor_deposito_cofre > saldo_total:  # Verificando se o valor do depósito é válido
        print(f'O VALOR DE DEPÓSITO DIGITADO É INVÁLIDO! Seu saldo atual é de R$ {saldo_total:.2f}.')
        print('Por favor, digite um valor válido!')
        valor_deposito_cofre = float(input('QUAL O VALOR DO DEPÓSITO? R$ '))  # Solicitando o valor do depósito novamente

    if valor_deposito_cofre > 0 and valor_deposito_cofre <= saldo_total:  # Se o valor de depósito for válido
        saldo_total -= valor_deposito_cofre  # Atualizando o saldo total
        saldo_total_cofre += valor_deposito_cofre  # Atualizando o saldo do cofre digital

        print(f'DEPÓSITO NO COFRE DIGITAL REALIZADO COM SUCESSO! Saldo atual do cofre digital: R$ {saldo_total_cofre:.2f}')  # Exibindo o saldo do cofre digital
        os.system('pause')  # Voltando para a tela inicial

        historico_operacoes.append(f'DEPÓSITO NO COFRE DIGITAL: R$ {valor_deposito_cofre:.2f}. SALDO COFRE DIGITAL: R$ {saldo_total_cofre:.2f}')  # Acrescentando na lista os dados do valor do depósito e do saldo do cofre digital

def consultar_saldo():
    global saldo_total  # Usando a variável global para exibir o saldo total
    global limite_credito  # Usando a variável global para exibir o limite de crédito

    print('------------------------------------------------------------')
    print('MACK BANK – CONSULTAR SALDO')
    print(f'SALDO TOTAL: R$ {saldo_total:.2f}')  # Exibindo o saldo total
    print(f'LIMITE DE CRÉDITO: R$ {limite_credito:.2f}')  # Exibindo o limite de crédito
    os.system('pause')  # Voltando para a tela inicial

def consultar_extrato():
    global historico_operacoes  # Usando a variável global para o histórico de operações

    print('------------------------------------------------------------')
    print('MACK BANK – CONSULTAR EXTRATO')

    if len(historico_operacoes) == 0:  # Verificando se não há operações registradas
        print('Não há operações realizadas.')
    else:
        for operacao in historico_operacoes:  # Exibindo todas as operações realizadas
            print(operacao)

    os.system('pause')  # Voltando para a tela inicial

while True:  # Loop infinito do menu inicial
    opcao = escolha_opcoes()  # Exibindo o menu inicial e armazenando a escolha do usuário

    if opcao == 1:  # Se a escolha for 1, vai para a função de cadastro de conta
        cadastro_conta()
    elif opcao == 2:  # Se a escolha for 2, vai para a função de depósito
        depositar()
    elif opcao == 3:  # Se a escolha for 3, vai para a função de saque
        sacar()
    elif opcao == 4:  # Se a escolha for 4, vai para a função de consulta de saldo
        consultar_saldo()
    elif opcao == 5:  # Se a escolha for 5, vai para a função de consulta de extrato
        consultar_extrato()
    elif opcao == 6:  # Se a escolha for 6, vai para a função de cofre digital
        cofre_digital()
    elif opcao == 7:  # Se a escolha for 7, encerra o programa
        print('Operações encerradas.')
        break  # Finalizando o loop e o programa
