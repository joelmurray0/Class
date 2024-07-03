def decrypt(text, key):
     height = len(text)//key
     output = ""
     left_str = ""
     for i in range(height):
          index = i
          left_over = len(text)%key
          while index < len(text):
               output += text[index]
               index += height
               if left_over > 0:
                    index += 1
                    left_over -= 1
     index = height
     for i in range(len(text)%key):
          left_str += text[index]
          index += height + 1
     
     return output + left_str

print(decrypt("Btkd eheebaenret s fic tonhhhrgiaae crn!", 8))
