"A text-based Python program to convert Strings into Morse Code."
#solution
# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', 
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', 
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', 
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}

# Reverse dictionary for Morse code to text conversion
REVERSE_MORSE_CODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

def string_to_morse_code(input_string):
    input_string = input_string.upper()
    morse_code = ''
    for char in input_string:
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
        else:
            morse_code += ' '  # For unknown characters, add a space
    return morse_code.strip()

def morse_code_to_string(morse_code):
    morse_code_words = morse_code.split(' / ')
    decoded_string = ''
    for word in morse_code_words:
        for code in word.split():
            if code in REVERSE_MORSE_CODE_DICT:
                decoded_string += REVERSE_MORSE_CODE_DICT[code]
        decoded_string += ' '
    return decoded_string.strip()

# Main program loop
while True:
    choice = input("Type '1' to convert string to Morse code, '2' to convert Morse code to string, or 'q' to quit: ")
    if choice == '1':
        user_input = input("Enter the string that you want convert into Morse Code: ")
        morse_code_output = string_to_morse_code(user_input)
        print(f"Morse Code: {morse_code_output}")
    elif choice == '2':
        morse_code_input = input("Enter the Morse Code that you want to convert into string (use '/' for spaces): ")
        string_output = morse_code_to_string(morse_code_input)
        print(f"Decoded String: {string_output}")
    elif choice.lower() == 'q':
        print("bye..take care!")
        break
    else:
        print("Invalid choice. Please select '1', '2', or 'q'.")
        
