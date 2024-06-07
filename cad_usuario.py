'''Crie um aplicativo de banco, onde o usuário possa:

- Cadastrar seu nome no aplicativo.
- Deletar seu nome do aplicativo.
- Entrar no aplicativo.

Ao entrar no aplicativo, o usuário pode:

- Consultar seu saldo(criar uma nova conta o saldo começa com R$ 0, 00
                      a consulta deverá exibir a data da consulta)
- Depositar valor.
- Sacar valor.
- Sair do programa.'''

#Importe das Bibliotecas:
import os
import time


#funções do programa:

# IDs das entradas
chaves = ('Nome', 'CPF', 'Telefone', 'E-mail', 'Profissão', 'Empresa','Conta-Cheque')
# Lista para armazenar os dados das pessoas
dados = []


def menu():
    while True:
        print(f"\n{'='*20} Bem Vindo ao Mamute Bank: {'='*20}")
        print(f"{'='*20} ESCOLHA UMA DAS OPÇÕES PARA INICIAR: {'='*20}")
        print("1. Quero ser cliente do banco")
        print("2. Deletar dados do usuario")
        print("3. entrar no aplicativo")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        os.system('cls')  # Limpa a tela

        if opcao == '1':
            inserir()
        elif opcao == '2':
            indice = int(input("Informe o índice da pessoa que deseja excluir: "))
            excluir_dados(indice)
        elif opcao == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


def inserir():
    # Coleta os dados da nova pessoa
    pessoa = {
        chaves[0]: input('Informe seu nome: '),
        chaves[1]: input('Informe o seu CPF: '),
        chaves[2]: input('Informe o  seu telefone: '),
        chaves[3]: input('Informe o seu e-mail: '),
        chaves[4]: input('Informe sua profissão: '),
        chaves[5]: input('Informe o nome da Empresa que você trabalha: '),
        chaves[6]: (input('Informe o valor do seu primeiro deposito em R$').replace(',','.'))
    }
    
    print('Inserindo Dados...')
    time.sleep(2)  # Espera por 2 segundos para simular a inserção
    dados.append(pessoa)  # Adiciona a nova pessoa à lista 'dados'
    print('Cadastro realizado com sucesso!')
    time.sleep(2)  # Espera por 2 segundos para que o usuário veja a mensagem


    while True:
        opcao = input(
            "Deseja voltar ao menu principal (s) ou sair do programa (n)? ").lower()
        if opcao == 's':
            break
        elif opcao == 'n':
            print("Saindo do programa...")
            # Espera por 2 segundos para simular saida do programa.
            time.sleep(2)
            exit()
        else:
            print("Opção inválida. Por favor, escolha 's' para voltar ao menu principal ou 'n' para sair do programa.")


def excluir_dados(indice):
    if indice < 1 or indice > len(dados):
        print("Índice inválido.")
        return

    dados.pop(indice - 1)  # Remove a pessoa pelo índice
    print(f"Item de índice {indice} removido com sucesso.")
    time.sleep(2)  # Espera por 2 segundos para que o usuário veja a mensagem
    os.system('cls')  # Limpa a tela


