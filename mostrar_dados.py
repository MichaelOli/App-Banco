import os
import time
from cad_usuario import *
from menu import *
from mostrar_dados import *


# funções do programa:

# IDs das entradas
chaves = ('Nome', 'CPF', 'Telefone', 'E-mail',
          'Profissão', 'Empresa', 'Conta-Cheque')
# Lista para armazenar os dados das pessoas
dados = []

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
