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
from cad_usuario import *


# IDs das entradas
chaves = ('Nome', 'CPF', 'Telefone', 'E-mail',
          'Profissão', 'Empresa', 'Conta-Cheque')
# Lista para armazenar os dados das pessoas
dados = []


def menu():
    while True:
        print(f"\n{'='*20} Bem Vindo ao Mamute Bank: {'='*20}")
        print(f"{'='*20} ESCOLHA UMA DAS OPÇÕES PARA INICIAR: {'='*20}")
        print("1. Quero ser cliente do banco")
        print("2. Deletar dados da conta")
        print("3. Dados da conta.")
        print("4. Atualizar Saldo da conta.")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        os.system('cls')  # Limpa a tela

        if opcao == '1':
            inserir ()
            print('Inserindo Dados...')
            time.sleep(2)  # Espera por 2 segundos para simular a inserção
            dados.append(inserir.pessoa)  # Adiciona a nova pessoa à lista 'dados'
            print('Cadastro realizado com sucesso!')
            # Espera por 2 segundos para que o usuário veja a mensagem
            time.sleep(2)
            time.sleep(2)
            os.system('cls')
        elif opcao == '2':
            indice = int(
                input("Informe o índice da pessoa que deseja excluir: "))
            excluir_dados(indice)
        elif opcao == '3':
            listar_dados()
            while True:
                opcao = input(
                    "Deseja voltar ao menu principal (s) ou sair do programa (n)? ").lower()
                if opcao == 's':
                    menu.menu()
                    break
                elif opcao == 'n':
                    print("Saindo do programa...")
                    # Espera por 2 segundos para simular saida do programa.
                    time.sleep(2)
                    exit()
                else:
                    print(
                        "Opção inválida. Por favor, escolha 's' para voltar ao menu principal ou 'n' para sair do programa.")

            # Pergunta ao usuário se deseja voltar ao menu principal ou sair do programa
            break
        elif opcao == '4':
            listar_dados()
            atualizar_dados()
            indice = int(
                input("Informe o índice da pessoa que deseja atualizar: "))
            atualizar_dados(indice)
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
        chaves[6]: (
            input('Informe o valor do seu primeiro deposito em R$ ').replace(',', '.'))
    }

    while True:
        opcao = input(
            "Deseja voltar ao menu principal (s) ou sair do programa (n)? ").lower()
        if opcao == 's':
            menu()
            break
        elif opcao == 'n':
            print("Saindo do programa...")
            # Espera por 2 segundos para simular saida do programa.
            time.sleep(2)
            exit()
        else:
            print("Opção inválida. Por favor, escolha 's' para voltar ao menu principal ou 'n' para sair do programa.")


def listar_dados():
    if not dados:
        # Informa se não há dados cadastrados
        print("Nenhum dado cadastrado...")
    else:
        print('Pesquisando Dados...')  # Mensagem de espera e tempo de espera
        time.sleep(2)  # Espera por 2 segundos para simular a pesquisa.
        for i, pessoa in enumerate(dados):
            print(f"{i+1}.")  # Exibe o número da pessoa na lista
            for chave, valor in pessoa.items():
                # Exibe cada par chave-valor da pessoa
                print(f"{chave}: {valor}")

        print('Dados listados com sucesso!')


def atualizar_dados(indice):
    if indice < 1 or indice > len(dados):
        print("Índice inválido.")
        return

    pessoa = dados[indice - 1]  # Acessa a pessoa pelo índice
    for chave in chaves:
        # Pergunta o novo valor de cada chave
        novo_valor = input(f"{chave[6]} atual ({pessoa[chave[6]]}): ")
        if novo_valor:
            # Atualiza o valor se o usuário forneceu uma nova entrada
            pessoa[chave[6]] = novo_valor


def excluir_dados(indice):
    if indice < 1 or indice > len(dados):
        print("Índice inválido.")
        return

    dados.pop(indice - 1)  # Remove a pessoa pelo índice
    print(f"Item de índice {indice} removido com sucesso.")
    time.sleep(2)  # Espera por 2 segundos para que o usuário veja a mensagem
    os.system('cls')  # Limpa a tela
