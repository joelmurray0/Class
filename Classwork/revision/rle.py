def rle(text):
     i=1
     count=1
     output=""
     while i != len(text):
          character_to_append = text[i-1]
          if text[i-1] == text[i]:
               count += 1
          else:
               output += f"{character_to_append} {count} "
               count=1
          i += 1
     if character_to_append == text[-1]:
          output += f"{character_to_append} {count+1}"
     else:
          output += f"{text[-1]} 1"
     
     return output

print(rle("CUTLASSES"))