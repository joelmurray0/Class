class Stack():
     def __init__(self):
          self.list = []
          self._size = 0

     def push(self, content):
          self.list.append(content)
          self._size += 1
          
     def pop(self):
          output = self.list[-1]
          del self.list[-1]
          self._size -= 1
          return output
     
     def peek(self):
          return self.list[-1]
     
     def get_size(self):
          return self._size
     
     def is_empty(self):
          output = False
          if self.get_size() == 0:
               output = True

def sort_stack(stack1, stack2):
     temp1 = stack1.peek()
     temp2 = stack2.peek()
     if temp1 < temp2:
          
