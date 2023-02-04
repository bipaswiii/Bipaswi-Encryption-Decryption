import unittest
import base64

class TestEncryptDecrypt(unittest.TestCase):
    def test_encryption(self):
        plain_text = "abc"
        key = 5
        cipher_text = ""
        for i in range(len(plain_text)):
            letter = plain_text[i]
            if letter.isdigit():
                char_code = int(letter)
                cipher_text += str((char_code + key) % 10)
            elif letter.isalpha() or (ord(letter) >= 33 and ord(letter) <= 126):
                char_code = ord(letter)
                if char_code + key > 126:
                    cipher_text += chr(char_code + key - 95)
                else:
                    cipher_text += chr(char_code + key)
            else:
                cipher_text += letter
        cipher_text = base64.b64encode(cipher_text.encode()).decode()
        self.assertEqual(cipher_text, "Zmdo")
    
    def test_decryption(self):
        cipher_text = "Zmdo"
        plain_text = ""
        key = 5
        cipher_text = base64.b64decode(cipher_text.encode()).decode()
        for i in range(len(cipher_text)):
            letter = cipher_text[i]
            char_code = ord(letter)
            if char_code in range(32, 127):
                if char_code - key < 32:
                    plain_text += chr(char_code - key + 95)
                else:
                    plain_text += chr(char_code - key)
            else:
                plain_text += letter
        self.assertEqual(plain_text, "abc")

if __name__ == '__main__':
    unittest.main()
