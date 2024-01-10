# O progama solicita o nome e o telefone do usuário.

# Após o cadastro, exibe a mensagem "paciente cadastrado com sucesso" e
# adiciona ao paciente a lista de Pacientes cadastrados 

# em em seguida, retorna ao menu principal

import csv
from datetime import datetime

class Paciente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Consulta:
    def __init__(self, paciente, dia, hora, especialidade):
        self.paciente = paciente
        self.dia = dia
        self.hora = hora
        self.especialidade = especialidade

pacientes_cadastrados = []
consultas_agendadas = []
ARQUIVO_PACIENTES = "pacientes.csv"
ARQUIVO_CONSULTAS = "consultas.csv"

def carregar_pacientes():
    try:
        with open(ARQUIVO_PACIENTES, newline='', encoding='utf-8') as arquivo:
            leitor_csv = csv.reader(arquivo)
            for linha in leitor_csv:
                nome, telefone = linha
                paciente = Paciente(nome, telefone)
                pacientes_cadastrados.append(paciente)
    except FileNotFoundError:
        pass  # O arquivo ainda não existe, será criado ao salvar os dados

def salvar_pacientes():
    with open(ARQUIVO_PACIENTES, mode='w', newline='', encoding='utf-8') as arquivo:
        escritor_csv = csv.writer(arquivo)
        for paciente in pacientes_cadastrados:
            escritor_csv.writerow([paciente.nome, paciente.telefone])

def carregar_consultas():
    try:
        with open(ARQUIVO_CONSULTAS, newline='', encoding='utf-8') as arquivo:
            leitor_csv = csv.reader(arquivo)
            for linha in leitor_csv:
                nome, telefone, dia, hora, especialidade = linha
                paciente = Paciente(nome, telefone)
                consulta = Consulta(paciente, dia, hora, especialidade)
                consultas_agendadas.append(consulta)
    except FileNotFoundError:
        pass  # O arquivo ainda não existe, será criado ao salvar os dados

def salvar_consultas():
    with open(ARQUIVO_CONSULTAS, mode='w', newline='', encoding='utf-8') as arquivo:
        escritor_csv = csv.writer(arquivo)
        for consulta in consultas_agendadas:
            escritor_csv.writerow([consulta.paciente.nome, consulta.paciente.telefone, consulta.dia, consulta.hora, consulta.especialidade])

def cadastrar_paciente():
    nome = input("Digite o nome do paciente: ")
    telefone = input("Digite o telefone do paciente: ")

    # Verifica se o paciente já está cadastrado pelo telefone
    for paciente in pacientes_cadastrados:
        if paciente.telefone == telefone:
            print("Paciente já cadastrado!")
            return

    paciente = Paciente(nome, telefone)
    pacientes_cadastrados.append(paciente)
    salvar_pacientes()
    print("Paciente cadastrado com sucesso!")

def listar_pacientes():
    print("Lista de Pacientes Cadastrados:")
    for i, paciente in enumerate(pacientes_cadastrados, start=1):
        print(f"{i}. {paciente.nome} - {paciente.telefone}")

def verificar_disponibilidade(dia, hora):
    for consulta in consultas_agendadas:
        if consulta.dia == dia and consulta.hora == hora:
            return False  # Dia e hora já agendados
    return True

def marcar_consulta():
    listar_pacientes()
    escolha = int(input("Escolha o número correspondente ao paciente para marcar a consulta: "))
    paciente = pacientes_cadastrados[escolha - 1]
    
    dia = input("Digite o dia da consulta: ")
    hora = input("Digite a hora da consulta: ")

    # Verifica se a data e a hora selecionadas estão disponíveis
    if not verificar_disponibilidade(dia, hora):
        print("Horário já agendado. Escolha outra data/hora.")
        return

    # Verifica se a data da consulta é posterior à data atual
    data_atual = datetime.now().strftime("%Y-%m-%d")
    if dia < data_atual:
        print("Não é possível agendar consultas retroativas.")
        return

    especialidade = input("Digite a especialidade desejada para a consulta: ")
    consulta = Consulta(paciente, dia, hora, especialidade)
    consultas_agendadas.append(consulta)
    salvar_consultas()
    print("Consulta agendada com sucesso!")

def listar_consultas():
    print("Lista de Consultas Agendadas:")
    for i, consulta in enumerate(consultas_agendadas, start=1):
        print(f"{i}. Paciente: {consulta.paciente.nome}, Dia: {consulta.dia}, Hora: {consulta.hora}, Especialidade: {consulta.especialidade}")

def cancelar_consulta():
    listar_consultas()
    escolha = int(input("Escolha o número correspondente à consulta para cancelar: "))
    consulta = consultas_agendadas[escolha - 1]
    print(f"Consulta marcada para {consulta.dia} às {consulta.hora} com {consulta.especialidade}.")
    confirmacao = input("Deseja realmente cancelar esta consulta? (S/N): ").upper()
    if confirmacao == "S":
        consultas_agendadas.remove(consulta)
        salvar_consultas()
        print("Consulta cancelada com sucesso!")

def menu_principal():
    carregar_pacientes()
    carregar_consultas()

    while True:
        print("\nMenu Principal:")
        print("1. Cadastrar um paciente")
        print("2. Marcar consulta")
        print("3. Cancelar consulta")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_paciente()
        elif opcao == "2":
            marcar_consulta()
        elif opcao == "3":
            cancelar_consulta()
        elif opcao == "4":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()
