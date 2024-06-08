
from menu import *
from cad_usuario import *
from mostrar_dados import *
from atualizandor_dados import *
from mostrar_dados import *
# IDs das entradas
chaves = ('Nome', 'CPF', 'Telefone', 'E-mail',
          'Profissão', 'Empresa', 'Conta-Cheque')
# Lista para armazenar os dados das pessoas
dados = []

def excluir_dados(indice):
    if indice < 1 or indice > len(dados):
        print("Índice inválido.")
        return

    dados.pop(indice - 1)  # Remove a pessoa pelo índice
    print(f"Item de índice {indice} removido com sucesso.")
    time.sleep(2)  # Espera por 2 segundos para que o usuário veja a mensagem
    os.system('cls')  # Limpa a tela
