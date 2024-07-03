ALPHABET = "abcdefghijklmnopqrstuvwxyz"
alphadict = {}

with open("FrequencyAnalysis\AlanTuring.txt", "r") as file:
  message = file.read()

for i in ALPHABET:
  alphadict[i] = 0

for char in message:
  if char.lower() in ALPHABET:
    alphadict[char.lower()] += 1
    
print(alphadict)