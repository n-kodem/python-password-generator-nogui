from random import choice
from pynput import keyboard
from os import system

numbers = [str(i) for i in range(0, 10)]
specialchars = [chr(i) for i in range(33, 48)] + [chr(i) for i in range(58, 65)] + [chr(i) for i in range(91, 97)] + [
    chr(i) for i in range(123, 127)]
largeletters = [chr(i) for i in range(65, 91)]
smallletters = [chr(i) for i in range(97, 123)]

options = [numbers, specialchars, largeletters, smallletters]
current = 0
selections = ["", "", "", ""]
do_again = True


def underline(*text):
    global current
    text = list(text)
    for i in range(len(text)):
        if i == current:
            text[i] = f'\033[4m{text[i]}\033[0m'
    return text


def changeCurrent(dirr):
    global current
    if dirr and (current < 3):
        current += 1
    if (not dirr) and (current != 0):
        current -= 1


def showSelection():
    global current
    print("Select password sing groups using arrows and X, press ENTER to submit, select nothing to select all types:")
    for i in underline(f'[{selections[0]}] Numbers',
                       f'[{selections[1]}] Specials',
                       f'[{selections[2]}] Large letters',
                       f'[{selections[3]}] Small letters'):
        print(i)
    print(selections)


def get_selected():
    to_use = []
    for i in range(len(selections)):
        if selections[i] == "X":
            to_use += options[i]
    if len(to_use) == 0:
        for i in range(len(selections)):
            to_use += options[i]
    return to_use


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
    elif str(key) == "Key.down":  # if key 'r' is pressed
        changeCurrent(True)
        system("cls")
        showSelection()

    elif str(key) == "Key.up":
        changeCurrent(False)
        system("cls")
        showSelection()

    elif "\'x\'" == str(key):
        if selections[current] == "":
            selections[current] = "X"
        else:
            selections[current] = ""
        system("cls")
        showSelection()
    elif "Key.enter" == str(key):
        return False
    # else:
    #     print(f'Key released: {key}')


def main():
    global current
    global do_again
    system("cls")
    showSelection()
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

    input()
    password_len = 0
    while True:
        try:
            system('cls')
            showSelection()
            password_len = int(input("Enter number of words to be used in your password: "))
            break
        except ValueError:
            continue
    print("".join([choice(get_selected()) for _ in range(password_len)]))
    if input("Want to get new password? Yes<X> | No: ").lower() != "no":
        do_again = False


if __name__ == '__main__':
    while do_again:
        main()
