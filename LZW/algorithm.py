def lzw_compress(text):
    dictionary = {chr(k): k for k in range(256)}
    encoded = list()
    s = text[0]
    for c in text[1:]:
        if s+c in dictionary:
            s =s+c
        else:
            print("> %s" %s)
            encoded.append(dictionary[s])
            print("found: %s compressed as %s" %(s,dictionary[s]))
            dictionary[s+c] = max(dictionary.values()) + 1
            print("New sequence %s indexed as %s" %(s+c, dictionary[s+c]))
            s = c
    encoded.append(dictionary[s])
    print("found: %s compressed as %s" %(s,dictionary[s]))
    return encoded

def lzw_decompress(encoded):
    reverse_dictionary = {k:chr(k) for k in range(256)}
    current = encoded[0]
    output = reverse_dictionary[current]
    print("Decompressed %s" % output)
    print(">%s" %output)
    for element in encoded[1:]:
        previous = current
        current = element
        if current in reverse_dictionary:
            s = reverse_dictionary[current]
            print("Decompressed %s" %s)
            output +=s
            print(">%s" % output)
            new_index = max(reverse_dictionary.keys()) + 1
            reverse_dictionary[new_index]=reverse_dictionary[previous] + s[0]
            print("New dictionary entry %s at index %s" % (reverse_dictionary[previous] + s[0],new_index))
        else:
            print("Not found:",current,"Output:",reverse_dictionary[previous] + reverse_dictionary[previous][0])
            s = reverse_dictionary[previous]+reverse_dictionary[previous][0]
            print("New dictionary entry %s at index %s" %(s, max(reverse_dictionary.keys())+1))
            reverse_dictionary[max(reverse_dictionary.keys())+1] = s
            print("Decompressed %s" %s)
            output +=s
            print(">%s" % output)
    return output
                  
text = "HasjdfgBjegsashdljh hsdjh ajhYusdlkjhlkjhslkjhhasdkjbvboooojgewgsoiuwgr"
compressed = lzw_compress(text)
print("\nCompressed: %s \n" % compressed)
print("\ndecompressed string: %s" %lzw_decompress(compressed))
print("original string was: %s" % text)