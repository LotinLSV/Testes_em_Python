import PySimpleGUI as sg

minha_lista = ['Lucas', 'Pedro', 'Jonas', 'Matheus']



def criar_janela_inical():
    sg.theme('DarkBlue4')
    l_Projeto =[
        [sg.Text('Nome do projeto:'), sg.Input('')]
    ]
    linha = [
        [sg.Checkbox(''), sg.Input(''), sg.Combo(minha_lista)]
    ]

    layout = [
        [sg.Frame('Projeto',layout=l_Projeto)],
        [sg.Frame('Tarefas',layout=linha,key='container')],
        [sg.Button('Nova tarefa'),sg.Button('Resetar')]
    ]

    return sg.Window('Todo list',layout=layout,finalize=True)

# criando janela

janela = criar_janela_inical()
#  criar regras
while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
        
    elif event == 'Nova tarefa':
        janela.extend_layout(janela['container'], 
                    [[sg.Checkbox(''), sg.Input(''), sg.Combo(minha_lista)]]          
                             )
    elif event == 'Resetar':
        janela.close()
        janela = criar_janela_inical()
        
