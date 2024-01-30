class Pet():
     def __init__(self, kind, legs_number):
          self.kind = kind
          self.legs_number = legs_number

     def start_running(self):
          print("Pet is running")
     
     def stop_running(self):
          print("Pet stopped")

dog = Pet("dog", 4)

monkey = Pet("monkey", 2)

dog.start_running()
monkey.stop_running()
