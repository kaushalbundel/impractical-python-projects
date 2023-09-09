#!/usr/bin/env python3
#implementation of rail-fence encryption and decryption

"""Encrypt a Civil war rail-fence cipher

<Implementation process description>


"""
#-----------------------------------------------------------------------------------------------------

#User Input
#string to be encrypted (Paste between the triple quotes)
plaintext = """Let us cross over the river and rest under the shade of the trees"""

#End of the User Input
#Do not add/edit beyond this line

#-----------------------------------------------------------------------------------------------------

def prep_plaintext(text:str):
    """convert plain text message by replacing the spaces and making the letters uppercase"""
    message = text.replace(" ", "").upper()
    print(f"The prepared plaintext message is: {message}")
    return message

def build_rails(message):
    """build rails by selectively picking alternate letters"""
    even  = message[::2]
    odd = message[1::2]
    rails = even + odd
    print(f"The rail code is: {rails}")
    return rails

def encrypt(rails):
    """final encrypted text with the string divided into letters of length 5"""
    encrypted_text = " ".join([rails[i:i+5] for i in range(0,len(rails), 5)])
    print(f"The final encrypted text is: {encrypted_text}")
    return encrypted_text

def main():
    """running the final program"""
    print(f"The plaintext message is: {plaintext}")
    message = prep_plaintext(plaintext)
    rails = build_rails(message)
    encrypt(rails)

if __name__ == '__main__':
   main()

#final output = LTSRS OETEI EADET NETEH DOTER EEUCO SVRHR VRNRS UDRHS AEFHT ES
