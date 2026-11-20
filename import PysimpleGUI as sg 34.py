import PySimpleGUI as sg
text = sg.popup_get_text('Escreva a palavra-passe', password_char='*')
sg.popup(f'Password:{text}')