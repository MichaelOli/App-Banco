from datetime import datetime

# Obtendo a data atual
data_atual = datetime.now()

# Formatando a data para o padrão brasileiro
data_formatada = data_atual.strftime("%d/%m/%Y")

usuarios = {}


def cadastrar_usuario(nome, cpf, telefone, email, profissao, empresa, deposito_inicial):
    deposito_inicial = deposito_inicial.replace(',', '')
    saldo_inicial = float(deposito_inicial)
    if cpf in usuarios:
        return "Usuário já cadastrado."
    usuarios[cpf] = {
        'nome': nome,
        'telefone': telefone,
        'email': email,
        'profissao': profissao,
        'empresa': empresa,
        'saldo': saldo_inicial,
        'data_criacao': data_formatada
    }
    return "Usuário cadastrado com sucesso."


def deletar_usuario(cpf):
    if cpf in usuarios:
        del usuarios[cpf]
        return "Usuário deletado com sucesso."
    return "Usuário não encontrado."


def consultar_saldo(cpf):
    if cpf in usuarios:
        saldo = usuarios[cpf]['saldo']
        data_consulta = data_formatada
        return f"Saldo: R$ {saldo:.2f}\nData da consulta: {data_consulta}"
    return "Usuário não encontrado."


def depositar_valor(cpf, valor):
    if cpf in usuarios:
        usuarios[cpf]['saldo'] += valor
        return f"Depósito de R$ {valor:.2f} realizado com sucesso."
    return "Usuário não encontrado."


def sacar_valor(cpf, valor):
    if cpf in usuarios:
        if usuarios[cpf]['saldo'] >= valor:
            usuarios[cpf]['saldo'] -= valor
            return f"Saque de R$ {valor:.2f} realizado com sucesso."
        return "Saldo insuficiente."
    return "Usuário não encontrado."
