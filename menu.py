from menu import *
from cad_usuario import *
from mostrar_dados import *
from atualizandor_dados import *
from mostrar_dados import *
from excluir_dados import *
# IDs das entradas
chaves = ('Nome', 'CPF', 'Telefone', 'E-mail','Profissão', 'Empresa', 'Conta-Cheque')
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
            dados.append(pessoa)  # Adiciona a nova pessoa à lista 'dados'
            print('Cadastro realizado com sucesso!')
            time.sleep(2)  # Espera por 2 segundos para que o usuário veja a mensagem
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
