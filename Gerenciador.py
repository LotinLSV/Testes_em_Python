import PySimpleGUI as sg

# Defina o layout da janela
layout = [
    [sg.Text('Nome:'), sg.InputText(key='nome')],
    [sg.Text('Idade:'), sg.InputText(key='idade')],
    [sg.Button('Adicionar Registro'), sg.Button('Remover Registro'), sg.Button('Salvar'), sg.Button('Sair')],
    [sg.Listbox([], size=(40, 6), key='registros')]
]

# Função para carregar registros do arquivo
def carregar_registros():
    try:
        with open('registros.txt', 'r') as arquivo:
            registros = [linha.strip() for linha in arquivo.readlines()]
    except FileNotFoundError:
        registros = []
    return registros

# Função para salvar registros no arquivo
def salvar_registros(registros):
    with open('registros.txt', 'w') as arquivo:
        arquivo.write('\n'.join(registros))

# Crie a janela
janela = sg.Window('App de Registro', layout)
registros = carregar_registros()

# Loop de eventos
while True:
    evento, valores = janela.read()

    if evento == sg.WIN_CLOSED or evento == 'Sair':
        break
    elif evento == 'Adicionar Registro':
        nome = valores['nome']
        idade = valores['idade']
        if nome and idade:
            registro = f'Nome: {nome}, Idade: {idade}'
            registros.append(registro)
            janela['registros'].update(values=registros)
            janela['nome'].update('')  # Limpa o campo de nome
            janela['idade'].update('')  # Limpa o campo de idade
    elif evento == 'Remover Registro':
        selecionados = janela['registros'].get_indexes()
        registros = [registro for i, registro in enumerate(registros) if i not in selecionados]
        janela['registros'].update(values=registros)
    elif evento == 'Salvar':
        salvar_registros(registros)

# Feche a janela
janela.close()
