"""
Caesar Cipher Encoder & Decoder 🔐
This script allows users to encode or decode text using the Caesar Cipher technique.
It takes user input for the message and the shift value, and supports both encryption
(encode) and decryption (decode) modes. 
- 🔁 Used `while` loop to allow repeated encode and decode until user exits 
- 🔤 Handled spaces properly - line 24
- ♻️ Used modulo `% 26` to wrap around the alphabet when shifting - line 32

"""

import string # python in-built module
alphabets = list(string.ascii_lowercase) # string constant
stopped = False 
while not stopped:
    while True:
            cipher_type = input("Type 'encode' to encrypt and 'decode' to decrypt: ").lower()
            if cipher_type in ['encode', 'decode']:
                break
            else:
                print("Please Enter a Valid Input!")
    def caesar_cipher(original_text,shift):
        word = ""
        for letter in original_text:
            if letter == " ":
                word += " "
            else:
                if cipher_type == 'encode':
                    shifted_position = alphabets.index(letter)+shift
                elif cipher_type == 'decode':
                    shifted_position = alphabets.index(letter)-shift
                shifted_position %= len(alphabets) # uses % 26
                word += alphabets[shifted_position]
        return word
            
    result = caesar_cipher(original_text = input("Type your message: ").lower(),shift = int(input("Type the shift number: ")))
    if cipher_type == 'encode':
       print(f"Here's the encoded result : {result}")
    else:
       print(f"Here's the decoded result : {result}")
    
    command = input("Type 'yes' if you want to go again. Otherwise type 'no'")
    if command == 'yes':
        continue 
    else:
        print("Exit!! You can now send your final result")
        break
    
    
            
        

    







