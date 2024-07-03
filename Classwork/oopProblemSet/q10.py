def display_menu():
     print("1. Enter encryption/decryption key \n2. Encrypt a message\n3. Decrypt a message\n4. Exit")
     
class EncryptDecrypt:
     def __init__(self, encr_decr_key):
          self._encr_decr_key = encr_decr_key

     @property
     def encr_decr_key(self):
          return self._encr_decr_key
     
     @encr_decr_key.setter
     def encr_decr_key(self, encr_decr_key):
          try:
               if 1 <= encr_decr_key <= 26:
                    self.encr_decr_key = encr_decr_key
          except TypeError:
               raise ValueError("Incorrect key input...")

     def encrypt(self, plaintext):
          plaintext.lower()
          ciphertext = ""
          for i in plaintext:
               new_letter = ""
               if ord(i) + self._encr_decr_key > ord("z"):
                    new_letter = chr(ord(i) + self._encr_decr_key - ord("z") + ord("a") - 1)
               else:
                    new_letter = chr(ord(i) + self._encr_decr_key)
               ciphertext += new_letter
          print(f"ciphertext: {ciphertext}")
     
     def decrypt(self, ciphertext):
          ciphertext.lower()
          plaintext = ""
          for i in ciphertext:
               new_letter = ""
               if ord(i) - self._encr_decr_key < ord("a"):
                    new_letter = chr(ord("z") - (ord("a") - ord(i) + self._encr_decr_key) + 1)
               else:
                    new_letter = chr(ord(i) - self._encr_decr_key)
               plaintext += new_letter
          print(f"plaintext: {plaintext}")


def main():
     exit = False
     while not exit:
          display_menu()
          choice = int(input("Enter choice. "))
          if choice == 1:
               key = int(input("Enter key. "))
               cipher = EncryptDecrypt(key)
          elif choice == 2:
               text = input("Enter input you want to encrypt. ")
               cipher.encrypt(text)
          elif choice == 3:
               text = input("Enter input you want to decrypt. ")
               cipher.decrypt(text)
          else:
               exit = True
     

if __name__ == "__main__":
     main()