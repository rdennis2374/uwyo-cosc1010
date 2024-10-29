# Ryan Dennis
# UWYO COSC 1010
# 10/29/2024
# HW 02
# Lab Section: 14
# Sources, people worked with, help given to: Stack Overflow
# your
# comments
# here

morse_code = {'A': '.-','B': '-...','C': '-.-.','D': '-..','E': '.','F': '..-.','G': '--.','H': '....','I': '..',
'J': '.---','K': '-.-','L': '.-..','M': '--','N': '-.','O': '---','P': '.--.','Q': '--.-','R': '.-.','S': '...','T': '-',
'U': '..-','V': '...-','W': '.--','X': '-..-','Y': '-.--','Z': '--..'}

def morse_message (word):
    message = ""
    for letter in word:
        if letter.upper() in morse_code:
            message += str(morse_code[letter.upper()])
            message += " "
        elif letter.upper() == " ":
                message += "  "
        else:
            print("Please enter a word")
            break
    print(message)
morse_message("")