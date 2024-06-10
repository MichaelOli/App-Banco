import os
import time
from cad_usuario import *
from datetime import datetime

data_atual = datetime.now()
data_formatada = data_atual.strftime("%d/%m/%Y")


def menu_principal():
    while True:
        print(f"{"="*20} Bem Vindo ao Mamute Bank {"="*20}")
        print("1. Quero ser cliente do banco")
        print("2. Deletar dados da conta")
        print("3. Dados da conta")
        print("4. Atualizar Saldo da conta")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        os.system('cls')

        if opcao == '1':
            inserir()
        elif opcao == '2':
            cpf = input("Informe o CPF da conta a ser deletada: ")
            print(deletar_usuario(cpf))
        elif opcao == '3':
            cpf = input("Informe o CPF da conta: ")
            print(consultar_saldo(cpf))
        elif opcao == '4':
            atualizar_saldo()
        elif opcao == '5':
            print("Saindo do programa...")
            time.sleep(2)
            break
        else:
            print("Opção inválida. Tente novamente.")


def inserir():
    nome = input('Informe seu nome: ')
    cpf = input('Informe o seu CPF: ')
    telefone = input('Informe o seu telefone: ')
    email = input('Informe o seu e-mail: ')
    profissao = input('Informe sua profissão: ')
    empresa = input('Informe o nome da Empresa que você trabalha: ')
    deposito_inicial = input(
        'Informe o valor do seu primeiro deposito em R$ ').replace(',', '.')

    print(cadastrar_usuario(nome, cpf, telefone,
          email, profissao, empresa, deposito_inicial))


def atualizar_saldo():
    cpf = input("Informe o CPF da conta: ")
    if cpf not in usuarios:
        print("Usuário não encontrado.")
        return

    while True:
        print("\n1. Depositar Valor")
        print("2. Sacar Valor")
        print("3. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            valor = float(input("Digite o valor para depósito: R$ "))
            print(depositar_valor(cpf, valor))
        elif opcao == '2':
            valor = float(input("Digite o valor para saque: R$ "))
            print(sacar_valor(cpf, valor))
        elif opcao == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu_principal()
