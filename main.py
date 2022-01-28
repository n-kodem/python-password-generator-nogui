from random import choice
from pynput import keyboard
from os import system

numbers = [str(i) for i in range(0, 10)]
specialchars = [chr(i) for i in range(33, 48)] + [chr(i) for i in range(58, 65)] + [chr(i) for i in range(91, 97)] + [
    chr(i) for i in range(123, 127)]
largeletters = [chr(i) for i in range(65, 91)]
smallletters = [chr(i) for i in range(97, 123)]

current = 0
selections = ["", "", "", ""]


def changeCurrent(dir):
    global current
    if dir and (current < 3):
        current += 1
    if (not dir) and (current != 0):
        current -= 1


def showSelection():
    global current
    print("Select password types:")
    print(f'[{selections[0]}] Numbers: {numbers}')
    print(f'[{selections[0]}] Specials: [\'' + "\', \'".join(specialchars) + '\']')
    print(f'[{selections[0]}] Large letters: {largeletters}')
    print(f'[{selections[0]}] Small letters: {smallletters}')
    print(selections)
    print(current)


def on_press(key):
    try:  # used try so that if user pressed other than the given key error will not be shown
        pass

    except AttributeError:
        print('special key pressed: {0}'.format(
            key))


def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    if str(key) == "Key.down":  # if key 'r' is pressed
        changeCurrent(True)

    if str(key) == "Key.up":
        changeCurrent(False)

    if "\'x\'" == str(key):
        if selections[current] == "":
            selections[current] = "X"
        else:
            selections[current] = ""
        system("cls")
        showSelection()
    else:
        print(f'Key released: {key}')


def main():
    global current
    system("cls")
    showSelection()
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


if __name__ == '__main__':
    main()
