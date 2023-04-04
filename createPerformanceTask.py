# Data abstraction for Morse code alphabet
MORSE_ALPHABET = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    '\'': '.----.',
    '!': '-.-.--',
    '/': '-..-.',
    '(': '-.--.',
    ')': '-.--.-',
    '&': '.-...',
    ':': '---...',
    ';': '-.-.-.',
    '=': '-...-',
    '+': '.-.-.',
    '-': '-....-',
    '_': '..--.-',
    '"': '.-..-.',
    '$': '...-..-',
    '@': '.--.-.'
}

# Morse code encoding
def encode_morse(text):
    encoded = []
    for letter in text.upper():
        if letter in MORSE_ALPHABET:
            encoded.append(MORSE_ALPHABET[letter])
        elif letter == ' ':
            encoded.append(' ')
        else:
            print()
            print(f'Cannot encode {letter}. Please try something different.')
    return encoded

# Morse code decoding
def decode_morse(morse):
    decoded = []
    for word in morse.split('   '):
        if word == '':
            decoded.append(' ')
            continue
        for code in word.split():
            for letter, seq in MORSE_ALPHABET.items():
                if code == seq:
                    decoded.append(letter)
                    error = 0
                    break
                else:
                    error = 1
        decoded.append(' ')
    if error == 1:
        return 'Error encountered while decoding. Please check characters and try again.'
    else:
        return ''.join(decoded[:-1])

def menu():
    options = [
        ('1', 'Translate text to Morse Code'),
        ('2', 'Translate Morse Code to text'),
        ('3', 'Translate text to Morse Code and back')
    ]

    for option in options:
        print(f'({option[0]}) {option[1]}')
    
    operation = input("Select an option from above by entering the corresponding number. To exit, ctrl+C. \n").lower()

    selected_option = None
    for option in options:
        if operation == option[0]:
            selected_option = option
            break
    
    if selected_option:
        if selected_option[0] == '1':
            text = input('Type the text you would like to translate to Morse Code. \n')
            encoded = ' '.join(encode_morse(text))
            print()
            print('Translated to Morse Code: \n' + encoded + '\n')
        elif selected_option[0] == '2':
            morse = input('Type in the Morse Code you would like to translate to text. \n')
            print()
            print('Translated to text: \n' + decode_morse(morse) + '\n')
        elif selected_option[0] == '3':
            text = input('Type the text you would like to translate to Morse Code and back. \n')
            encoded = ' '.join(encode_morse(text))
            print()
            print('Morse Code: \n' + encoded + '\n')
            decoded = decode_morse(encoded)
            print('Decoded text: \n' + decoded + '\n')
    elif operation == '':
        return
    else:
        print('Invalid option')

    # Repeat the menu
    menu()

menu()