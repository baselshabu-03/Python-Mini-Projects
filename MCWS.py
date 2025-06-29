# Code Refactored
import winsound
import time

# Create a Dictionary by inserting the Alphabets, Numbers & Symbols
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '.-.-.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-.', '$': '...-..-',
    '@': '.--.-.', '#': '-.-.--', '*': '-.-.-', '{': '-.-.--.', '}': '-.-.--.-', '%': '-..-.', '~': '.-.-.-.-', 
    '`': '.----.', '[': '-.--.-', ']': '-.--.-.'
}

# Create a function to convert Alphabets, Numbers & Symbols into Morse Code
def convert_to_morse(text):
    morse_text = ''
    for char in text:
        if char.upper() in morse_code:
            morse_text += morse_code[char.upper()] + ' / '
            play_sound(morse_code[char.upper()])
        else:
            morse_text += char + ' '
    return morse_text.strip()

# Function to play sound for Morse code
def play_sound(morse_char):
    for symbol in morse_char:
        if symbol == '.':
            winsound.Beep(1000, 200)  # Beep for dot
        elif symbol == '-':
            winsound.Beep(1000, 600)  # Beep for dash
        time.sleep(0.2)  # Pause between parts

# Getting input from User
user_input = input("Enter the Phrase to convert to Morse Code: ")

# Converting the input to Morse Code
morse_output = convert_to_morse(user_input)

# Print the Output
print("Morse Code:", morse_output)

# Create a function to convert Morse Code into Alphabets, Numbers & Symbols
def convert_from_morse(morse_text):
    text = ''
    morse_words = morse_text.split(' / ')
    for morse_word in morse_words:
        morse_chars = morse_word.split(' ')
        for morse_char in morse_chars:
            for char, code in morse_code.items():
                if code == morse_char:
                    text += char
                    break
        text += ' '
    return text.strip()
