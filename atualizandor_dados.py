import os
import time
from cad_usuario import *
from menu import *
from atualizandor_dados import *

# funções do programa:

# IDs das entradas
chaves = ('Nome', 'CPF', 'Telefone', 'E-mail','Profissão', 'Empresa', 'Conta-Cheque')
# Lista para armazenar os dados das pessoas
dados = []

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
