# ITU Morse code dictionary
ITU_MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', '.': '.-.-.-', ',': '--..--', '?': '..--..',
    "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.',
    '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': '/'  # Word separator
}


# Function to translate Morse code to nucleotides
def morse_to_nucleotide_itu(morse_code):
    nucleotide_mapping = {'.': 'C', '-': 'T', '/': 'A', ' ': 'G'}
    nucleotide_sequence = ''.join(nucleotide_mapping[char] for char in morse_code if char in nucleotide_mapping)
    return nucleotide_sequence


# Function to convert text to ITU Morse code and nucleotide sequence
def text_to_nucleotide_itu(text):
    # Convert to uppercase to match ITU_MORSE_CODE_DICT
    text = text.upper()

    # Convert text to ITU Morse code
    morse_code = ' '.join(ITU_MORSE_CODE_DICT[char] for char in text if char in ITU_MORSE_CODE_DICT)

    # Convert Morse code to nucleotide sequence
    nucleotide_sequence = morse_to_nucleotide_itu(morse_code)

    return morse_code, nucleotide_sequence


# Example input
input_text = "Let man have dominion over the fish of the sea, and over the fowl of the air, and over every living thing that moves upon the earth."
morse_code, nucleotide_sequence = text_to_nucleotide_itu(input_text)

# Output results
print("Input Text:", input_text)
print("ITU Morse Code:", morse_code)
print("Nucleotide Sequence:", nucleotide_sequence)
print("\n~~~~~ INFORMATION DENSITY CALCULATION ~~~~~")
print("Number of nucleotides in sequence", len(nucleotide_sequence))
print("Assume 5 bits are sufficient to encode a character (letters, digits, and possibly punctuation and their binary representation before they are encoded into morse code) \nassumunption is made before encoding to morse code because morse code has varied length coding scheme \nASCII or other binary encoding schemes often use 7 or 8 bits per character, but here, only 5 bits are sufficient for the set of characters being used (likely uppercase English letters and maybe a few symbols)\ntotal of 32 distinct characters=2^5 ")
information_density = (5 * len(input_text)/len(nucleotide_sequence))
print("Information Density (bits/nucleotide) = ", information_density)



