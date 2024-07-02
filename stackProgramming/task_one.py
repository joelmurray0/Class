class Stack():
     def __init__(self):
          self.list = []

     def push(self, content):
          self.list.append(content)
     
     def pop(self):
          output = self.list[-1]
          del self.list[-1]
          return output
     
if __name__ == "__main__":
     input_string = input("Enter a string. \n")
     output_string = ""
     string_stack = Stack()
     for char in input_string:
          string_stack.push(char)
     for _ in range(len(input_string)):
          output_string += string_stack.pop()
     print(output_string)