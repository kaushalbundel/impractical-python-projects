#!/usr/bin/env python3
#Decryption algorithm for rail fence cipher
"""Decrytping rail fence Cipher
#-----------------------------------------------------------------------------------------------------

"""

#User Input (mentioned the encrypted text within the quotes)
encrypted_text = """LTSRS OETEI EADET NETEH DOTER EEUCO SVRHR VRNRS UDRHS AEFHT ES"""

#-----------------------------------------------------------------------------------------------------
import math

def prep_decrypt(encrypted_text):
    """aggregates the encrypted text into one single string"""
    combined_text = encrypted_text.replace(" ", "")
    # combined_text = "".join(encrypted_text.split()) #two methods of removing the spaces and combining all the letters
    print(f"The aggregated combined text is: {combined_text}")
    return combined_text

def divide_string(combined_text):
    """divides the combined text into two strings"""
    length_text = math.ceil(len(combined_text)/2)
    text_1 = combined_text[:length_text].lower()
    text_2 = combined_text[length_text:].lower()
    print(f"The two strings are: {text_1} and {text_2}")
    return text_1, text_2

def decrypt(text_1, text_2):
    """decrypts the text by arranging the text in one single line"""
    word = ""
    for i, j in zip(text_1, text_2):
        word += i + j
    print(f"The word is: {word}")
    return word

def main():
    combined_text = prep_decrypt(encrypted_text)
    text_1, text_2 = divide_string(combined_text)
    return decrypt(text_1, text_2)

if __name__ == '__main__':
    main()

#final result = "letuscrossovertheriverandrestundertheshadeofthetrees"
#As of now I am not able to divide the text into different words but someday....
