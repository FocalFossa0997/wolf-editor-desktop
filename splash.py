import PySimpleGUI as sg
import time

sg.theme('DarkPurple')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Image('WolfEditor.gif')]]

# Create the Window
window = sg.Window('Wolf Editor Startup', layout, disable_minimize=True, no_titlebar=True)
window.read()
print('Sleeping...')
time.sleep(5)
window.close()