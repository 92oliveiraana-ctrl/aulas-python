import PySimpleGUI as sg
text = sg.popup_get_text('Revele a palavra secreta', password_char='?')
sg.popup(f'Password:{text}')
