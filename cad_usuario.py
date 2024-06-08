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
from menu import *
from cad_usuario import *
from mostrar_dados import *
from atualizandor_dados import *
from mostrar_dados import *


#funções do programa:

# IDs das entradas
chaves = ('Nome', 'CPF', 'Telefone', 'E-mail', 'Profissão', 'Empresa','Conta-Cheque')
# Lista para armazenar os dados das pessoas
dados = []


def inserir():
    # Coleta os dados da nova pessoa
    pessoa = {
        chaves[0]: input('Informe seu nome: '),
        chaves[1]: input('Informe o seu CPF: '),
        chaves[2]: input('Informe o  seu telefone: '),
        chaves[3]: input('Informe o seu e-mail: '),
        chaves[4]: input('Informe sua profissão: '),
        chaves[5]: input('Informe o nome da Empresa que você trabalha: '),
        chaves[6]: (input('Informe o valor do seu primeiro deposito em R$ ').replace(',','.'))
    }
    
    


    while True:
        opcao = input(
            "Deseja voltar ao menu principal (s) ou sair do programa (n)? ").lower()
        if opcao == 's':
            menu ()
            break
        elif opcao == 'n':
            print("Saindo do programa...")
            # Espera por 2 segundos para simular saida do programa.
            time.sleep(2)
            exit()
        else:
            print("Opção inválida. Por favor, escolha 's' para voltar ao menu principal ou 'n' para sair do programa.")
