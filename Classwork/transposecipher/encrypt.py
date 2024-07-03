def encrypt(text, key):
     output = ""
     for i in range(key):
          index = i
          while index < len(text):
               output += text[index]
               index += key
     return output

print(encrypt("Beating the chickens harder than before!", 8))