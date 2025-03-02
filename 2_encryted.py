
import string

def decrypt(text, k):
    result = ""
    alphabet_upper = string.ascii_uppercase
    alphabet_length = len(alphabet_upper)
    
    for char in text:
        index = alphabet_upper.index(char)
        decrypt_index = (index - k) % alphabet_length  
        result += alphabet_upper[decrypt_index]
    
    return result


decrypted_text = (decrypt("UCTCK", 2))
print("Decrypted Text:", decrypted_text)
