import sys


def morse_code(text):
    """
    Convert a given text to Morse code.
    The function takes a string as input and
    returns its Morse code representation.
    """
    MORSE_CODE_DICT = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', ' ': '/',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.'
    }
    return ' '.join(MORSE_CODE_DICT[char] for char in text)


def main():
    """
    Takes a string as input and converts it to Morse code.
    """
    if len(sys.argv) != 2:
        print("AssertionError: more than one argument is provided")
        return
    try:
        print(morse_code(sys.argv[1].upper()))
    except Exception:
        print("AssertionError: the arguments are bad")
        return


if __name__ == "__main__":
    main()
