import passgen
import os

p = passgen
SYMBOLS = ''

def start():
    print('[1] Generate password\n'
    + '[2] Settings\n'
    + '[3] About\n'
    + '[4] Exit')
    option = input('--> ')
    if option == '1':
        gen()
    elif option == '2':
        settings()
    elif option == '3':
        about()
    elif option == '4':
        exit()
    else:
        print("-->Unknown option<--")

def settings():
    global SYMBOLS
    invalid = True
    while invalid:
        SYMBOLS = input('Do you want to have symbols? ($@!€%&-_.,) y/n: ')
        if SYMBOLS == "y" or SYMBOLS == "yes":
            invalid = False
            SYMBOLS = "$@!€%&-_.,"
        elif SYMBOLS == "n" or SYMBOLS == "no":
            invalid = False
            SYMBOLS = ""
        else:
            return print("-->Unknown option<--")

def about():
    print('░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n'
        + '░        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░     ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n'
        + '▒   ▒▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒\n'
        + '▒   ▒▒▒▒   ▒▒▒▒   ▒▒▒▒▒▒     ▒▒▒     ▒▒  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒   ▒   ▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒   ▒▒   ▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒   ▒▒   ▒▒\n'
        + '▓        ▓▓▓▓   ▓▓   ▓▓   ▓▓▓▓▓   ▓▓▓▓▓   ▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓   ▓▓▓   ▓▓   ▓▓▓▓▓▓▓▓   ▓▓▓   ▓▓▓   ▓▓▓▓▓▓▓   ▓▓▓▓▓▓   ▓▓▓▓▓   ▓\n'
        + '▓   ▓▓▓▓▓▓▓▓   ▓▓▓   ▓▓▓▓    ▓▓▓▓    ▓▓   ▓▓▓      ▓         ▓▓▓   ▓▓   ▓▓▓▓▓▓▓▓▓   ▓   ▓▓▓▓   ▓▓▓▓▓▓▓   ▓▓▓▓▓▓   ▓▓▓▓▓▓   \n'
        + '▓   ▓▓▓▓▓▓▓▓   ▓▓▓   ▓▓▓▓▓▓   ▓▓▓▓▓   ▓▓   ▓▓▓▓  ▓▓▓  ▓▓▓▓▓▓▓▓▓▓   ▓▓   ▓▓▓▓▓▓▓▓▓▓     ▓▓▓▓▓   ▓▓▓▓▓▓▓   ▓▓▓▓▓▓▓   ▓▓▓▓   ▓\n'
        + '█   ██████████   █    █      ██      ████      ███████     ████    ██   ███████████   █████     █  ██     █  ██████    ████\n'
        + '███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████\n\n\n')
    print('Author: l0wGK (https://github.com/l0wGK)\n\n'
        + "Change log (v1.1.0):\nIt's now possible to generate passwords with a length of 256 characters.\n"
        + "New start menu\n"
        + "New settings\n"
        + "Removed some symbols\n\n\n")
    input('Press enter to leave this page\n\n')

def gen():
    global SYMBOLS
    invalid = True
    while invalid:
        try:
            num = int(input("Password length: "))
            if num >= 257 or num <= 7:
                print("-->Password length must be between 8-256 characters<--")
        
            else:
                password = p.generate(num, SYMBOLS)
                p.copy(password)
                invalid = False
                print("-->Password copied to clipboard<--")
            
        except:
            print("-->Input was not an integer<--")

if __name__ == '__main__':
    while True:
        start()