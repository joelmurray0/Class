class Info:
     def __init__(self, user_text):
          self._user_text = user_text
     
     @property
     def user_text(self):
          return self._user_text
     
     @user_text.setter
     def user_text(self, user_text):
          if not user_text:
               raise ValueError("Please input text")
          self._user_text = user_text
     
     def get_spaces(self):
          count = self.get_words() - 1
          if self._user_text[0] == " ":
               count += 1
          if self._user_text[-1] == " ":
               count += 1
          return count

     def get_words(self):
          sep_par_spaces = self._user_text.split(" ")
          return len(sep_par_spaces)
     
     def remove_spaces(self):
          return 0, self._user_text.replace(" ", "")

     def get_vowels(self):
          counter, text = self.remove_spaces()
          for i in text:
               if i in "aeiou":
                    counter += 1
          return counter
     
     def get_letters(self):
          _, text = self.remove_spaces()
          return len(text)
     
def main():
     input_text = input("Enter text to be processed.\n")
     text = Info(input_text)
     print(f"Spaces: {text.get_spaces()} \nWords: {text.get_words()} \nVowels: {text.get_vowels()} \nLetters: {text.get_letters()}")

if __name__ == "__main__":
     main()