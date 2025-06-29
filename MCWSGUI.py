import tkinter as tk
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
            play_sound(morse_code[char.upper()])  # Play sound for each Morse character
        else:
            morse_text += char + ' '
    return morse_text.strip()

# Function to play sound for Morse code
def play_sound(morse_char):
    for symbol in morse_char:
        if symbol == '.':
            winsound.Beep(1000, 200)  # Dot sound
        elif symbol == '-':
            winsound.Beep(1000, 600)  # Dash sound
        time.sleep(0.2)  # Space between parts of the same letter
    time.sleep(0.6)  # Space between letters

# Create the GUI
def generate_morse_code():
    user_input = entry.get()
    morse_output = convert_to_morse(user_input)
    output_label.config(text="Morse Code: " + morse_output)

# Setting up the Tkinter window
root = tk.Tk()
root.title("Morse Code Generator")

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

generate_button = tk.Button(root, text="Convert to Morse Code", command=generate_morse_code)
generate_button.pack(pady=10)

output_label = tk.Label(root, text="")
output_label.pack(pady=10)

root.mainloop()
