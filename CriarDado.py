import PySimpleGUI as sg

# Defina o layout da janela
layout = [
    [sg.Text('Digite algo:'), sg.InputText(key='input')],
    [sg.Button('Salvar'), sg.Button('Sair')]
]

# Crie a janela
janela = sg.Window('Exemplo de PySimpleGUI', layout)

# Loop de eventos
while True:
    evento, valores = janela.read()

    if evento == sg.WIN_CLOSED or evento == 'Sair':
        break
    elif evento == 'Salvar':
        dado = valores['input']
        with open('dados.txt', 'w') as arquivo:
            arquivo.write(dado)
            sg.popup('Dados salvos com sucesso!')

# Feche a janela
janela.close()
