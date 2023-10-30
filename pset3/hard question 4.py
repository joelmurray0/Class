flag = True

def check_palidrome(word):
     palindrome = True
     length = len(word)

     for i in range(length//2):
          if not (word[i] == word[-1-i]):
               palindrome = False

     return palindrome

phrase = input("Enter the word/words you want to check are palindrome.")

phrase = phrase.replace(" ", "")

flag = check_palidrome(phrase)

if flag:
     print("Your word is a palindrome!")
else:
     print("Unfortunately, your word is not a palindrome.")
