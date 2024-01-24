import PySimpleGUI as sg
'''
# STEP 1 - create the window, read the window, close the window.
event, values = sg.Window('My single-line GUI!',
                    [[sg.Text('My one-shot window.')],
                     [sg.InputText(key='-IN-')],
                     [sg.Submit(), sg.Cancel()]]).read(close=True)

# finally show the input value in a popup window
sg.popup('You entered', values['-IN-'])

#teste2
layout = [[sg.Text('My one-shot window.')],
                 [sg.InputText()],
                 [sg.Submit(), sg.Cancel()]]

window = sg.Window('Window Title', layout)

event, values = window.read()
window.close()

text_input = values[0]
sg.popup('You entered', text_input)
 teste3 
 
 
sg.theme('BluePurple')

layout = [[sg.Text('Your typed chars appear here:'), sg.Text(size=(15,1), key='-OUTPUT-')],
          [sg.Input(key='-IN-')],
          [sg.Button('Show'), sg.Button('Exit')]]

window = sg.Window('Pattern 2B', layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        # Update the "output" text element to be the value of "input" element
        window['-OUTPUT-'].update(values['-IN-'])

window.close()'''
#Temas
#sg.theme_previewer()
sg.theme('Dark Brown')
layout = [[sg.Text('Theme Browser')],
          [sg.Text('Click a Theme color to see demo window')],
          [sg.Listbox(values=sg.theme_list(), size=(20, 12), key='-LIST-', enable_events=True)],
          [sg.Button('Exit')]]

window = sg.Window('Theme Browser', layout)

while True:  # Event Loop
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    sg.theme(values['-LIST-'][0])
    sg.popup_get_text('This is {}'.format(values['-LIST-'][0]))

window.close()


