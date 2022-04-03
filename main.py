from threading import Thread as Th
from time import sleep
from PySimpleGUI import (
    theme,
    Window,
    Text,
    Button,
    WIN_CLOSED,
)

from pynput import keyboard as kb

# listener keyboard


# constant
counterKey = 0


def on_press(key):
    global counterKey
    try:
        print(key.char)
        counterKey += 1
    except:
        print(key)
        counterKey += 1


def listenerKeyBoard():
    with kb.Listener(
            on_press=on_press
    ) as listener:
        listener.join()


def layout():
    return [
        [Text('', key='-UPDATE-')],
        [Button('Reset', key='-RESET-')]
    ]


window = Window('counter keyboard', layout())


def prueba():
    global counterKey
    while True:
        if True:
            window.write_event_value('-UPDATE-', counterKey)
            sleep(0.1)


def initGUI():
    global counterKey
    theme('reddit')
    while True:
        event, values = window.read()

        if event == '-RESET-':
            counterKey = 0

        if event == WIN_CLOSED:
            break

        if event == '-UPDATE-':
            window['-UPDATE-'].update(str(counterKey))


def sepProcess():
    Th(target=prueba, daemon=True).start()
    Th(target=initGUI).start()
    Th(target=listenerKeyBoard).start()


if __name__ == '__main__':
    sepProcess()
