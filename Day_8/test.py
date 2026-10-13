'''
def encrypt(original_text, shift_amount):
    cipher_text = ''
    
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")
        
encrypt(original_text=text, shift_amount=shift)

def decrypt(original_text, shift_amount):
    cipher_text = ''
    
    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")
     
     
#encrypt(original_text=text, shift_amount=shift)    
decrypt(original_text=text, shift_amount=shift) '''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def caesar(original_text, shift_amount, encode_or_decode):
        
    if encode_or_decode == "decode":
        shift_amount *= -1
            
    cipher_text = ''
            
    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
        else:
            cipher_text += letter
    print(f"Here is the {encode_or_decode}d result: {cipher_text}")

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    
    if direction == "exit":
        print("Good bye!")
        break
        
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)