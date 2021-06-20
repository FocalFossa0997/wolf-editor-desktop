import PySimpleGUI as sg
import os
import sys

from PySimpleGUI.PySimpleGUI import InputText, WIN_CLOSED, WIN_CLOSE_ATTEMPTED_EVENT, WIN_X_EVENT

print('Attempting to setup the window...')
sg.theme('DarkGrey9')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Wolf Editor Desktop')],
            [sg.Button('New'), sg.InputText(key='savePath'), sg.Button('Save'), sg.InputText(key='loadPath'), sg.Button('Load'), sg.Button('About'), sg.Button('Found a bug?'), sg.Button('Quit')],
            [sg.Multiline(size=(158, 42), key='MainDocument')]
]

# Function for creating error messages
def errorMessage(title, message):
    elayout = [[sg.Text(message)], # Create the main text for the error message.
    [sg.Button('Dismiss')]]
    ewindow = sg.Window(title, elayout) # Create the error message window

    while True:
        eevent, evalues = ewindow.read()
        if eevent == sg.WIN_CLOSED or eevent == 'Dismiss': # if user closes window or clicks dismiss in the window
            break
    
    ewindow.close()

# Create the Window
print('Creating the window.')
window = sg.Window('Wolf Editor Desktop', layout, icon='icon.ico')
# Event Loop to process 'events' and get the 'values' of the inputs
        
while True:    
    event, values = window.read()
    
    if event == WIN_CLOSED:
        break
    
    if event == 'About': # of user clicks about:
        alayout = [  [sg.Text('Wolf Editor Desktop is the offline, self-contained version of Wolf Editor.\nWolf editor is a simple text editor creted by Barry Piel (a.k.a Focal Fossa).\nYou are running version 1.2 Check the changelog.txt file for a list of all new changes.')],
            [sg.Button('Dismiss')]
        ] # Create our about window layout

        awindow = sg.Window('Wolf Editor About', alayout) # Create the window

        while True:
            aevent, avalues = awindow.read()
            if aevent == sg.WIN_CLOSED or aevent == 'Dismiss': # if user closes window or clicks dismiss in the about window
                break
        
        awindow.close() # Close the about window
    
    if event == 'Quit': # of user clicks quit:
        qlayout = [  [sg.Text('Are you sure you want to quit? Any unsaved changes will be lost!')],
                [sg.Button('No'), sg.Button('Yes')]
            ] # Setup the layout for the new quit conformation window

        qwindow = sg.Window('Really Quit?', qlayout) # Create the quit conformation window
        
        while True:
            qevent, qvalues = qwindow.read()

            if qevent == 'Yes': # When the user says yes to quitting
                sys.exit(0)
                #exit()
            if qevent == sg.WIN_CLOSED or qevent == 'No': # When the user says no to quitting
                break
        qwindow.close() # Close the window after it is needed

    if event == 'New': # of user clicks New:
        nlayout = [  [sg.Text('Are you sure you want to create a new file? Any unsaved changes will be lost!')],
            [sg.Button('No'), sg.Button('Yes')]
        ] # Setup the layout for the new new file conformation window

        nwindow = sg.Window('Make a new file?', nlayout) # Create the new file conformation window

        while True:
            
            nevent, nvalues = nwindow.read()

            if nevent == 'Yes': # When the user says yes to making a new file
                window.FindElement('MainDocument').Update('')
                window.FindElement('savePath').Update('')
                window.FindElement('loadPath').Update('')
                break
            if nevent == sg.WIN_CLOSED or nevent == 'No': # When the user says no to making a new file
                break
        nwindow.close()

    if event == 'Found a bug?':
        errorMessage('Found a bug?', 'Report it on the `issues` part Wolf Editor`s github page.')
    
    if event == 'Save':
        filePathToSave = values['savePath']
        
        if filePathToSave == '':
            errorMessage('Warning', 'You cannot save a file without specifying a file path.')
        else:
            if os.path.exists(filePathToSave):
                loaded_file = open(filePathToSave, 'w')
                loaded_file.write(values['MainDocument'])
                loaded_file.close()
                errorMessage('Wolf Editor', 'Successfully saved file') 
            
            else:
                print('The file does not exist, create new file before continue')
                os.system('echo "" > ' + filePathToSave)
                loaded_file = open(filePathToSave, 'w')
                loaded_file.write(values['MainDocument'])
                loaded_file.close()
                errorMessage('Wolf Editor', 'Successfully saved file')

    if event == 'Load':
        filePathToLoad = values['loadPath']
        
        if filePathToLoad == '':
            errorMessage('Warning', 'You cannot load a file without specifying a file path.')
        else:
            if os.path.exists(filePathToLoad):
                loaded_file = open(filePathToLoad, 'r')
                loaded_file_data = loaded_file.read()
                window.FindElement('MainDocument').Update(loaded_file_data)
                window.FindElement('savePath').Update(filePathToLoad)
                loaded_file.close()
                errorMessage('Wolf Editor', 'Successfully loaded file')
            
            else:
                errorMessage('Warning', 'The file you`re trying to load does not exist.')
            

window.close()