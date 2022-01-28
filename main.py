from random import choice

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

numbers = [str(i) for i in range(0, 10)]
specialchars = [chr(i) for i in range(33, 48)] + [chr(i) for i in range(58, 65)] + [chr(i) for i in range(91, 97)] + [chr(i) for i in range(123, 127)]
largeletters = [chr(i) for i in range(65, 91)]
smallletters = [chr(i) for i in range(97, 123)]


def main():
    # Use a breakpoint in the code line below to debug your script.
    print(f'NUMS: {numbers}')
    print(f'specials: [\'' + "\', \'".join(specialchars) + '\']')
    print(f'large letters: {largeletters}')
    print(f'small letters: {smallletters}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
