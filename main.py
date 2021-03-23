from PySimpleGUI import PySimpleGUI as sg
import os

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Tempo em Minutos'), sg.Input(key='tempo', size=(30, 1))],
    [sg.Text('')],
    [sg.Button('Agendar Desligamento')]
]
# Janela
janela = sg.Window('Tela de Login', layout)

# Ler os Eventos
# manter a interface ativa
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Agendar Desligamento':
        if valores['tempo'] > '0':
            time = valores['tempo']
            time = int(time) * 60
            os.system(f"shutdown /s /t {time}")
            # print(time)
            sg.popup('Desligamento em ' + valores['tempo'] + ' minutos')
            break


# client= int(input("Digite o tempo em minutos: "))
# tempo= client * 60
# os.system(f"shutdown /s /t {tempo}")
