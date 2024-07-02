class Stack():
     def __init__(self):
          self.list = []

     def push(self, content):
          self.list.append(content)
     
     def pop(self):
          output = self.list[-1]
          del self.list[-1]
          return output
     
     def get_size(self):
          return len(self.list)
     
if __name__ == "__main__":
     decimal_number = int(input("Enter decimal number to be converted. \n"))
     binary_number = ""
     binary_number_stack = Stack()
     quotient = decimal_number
     while quotient != 0:
          remainder = quotient % 2
          quotient //=  2
          binary_number_stack.push(remainder)
     for _ in range(binary_number_stack.get_size()):
          binary_number += f"{binary_number_stack.pop()}"
     print(binary_number)