import sys

while True:
    print('Please enter your name.')
    response = raw_input()
    if response == 'Tess':
        print('Hello, ' + response + '.')
        sys.exit()
    elif response == 'tess':
        print('Hello, ' + response + '.')
        sys.exit()
    print('You typed ' + response + '. ' + 'That is not your name.')
