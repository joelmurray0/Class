class Pet():
     def __init__(self, kind, legs_number):
          self._kind = kind
          self._legs_number = legs_number

     @property
     def kind(self, kind):
          return self._kind

     @kind.setter
     def kind(self, kind):
          if not kind:
               raise ValueError("Enter a kind")
          self._kind = kind
     
     @property
     def legs_number(self, legs_number):
          return self._legs_number

     @legs_number.setter
     def legs_number(self, legs_number):
          if legs_number < 0:
               raise ValueError("Enter a number of legs")
          self._legs_number = legs_number

     def start_running(self):
          print("Pet is running")
     
     def stop_running(self):
          print("Pet stopped")

def main():
     dog = Pet("dog", 4)
     monkey = Pet("monkey", 2)

     dog.start_running()
     monkey.stop_running()

if __name__ == "__main__":
     main()