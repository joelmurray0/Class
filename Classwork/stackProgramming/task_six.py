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
     
     def top(self):
          return self.list[-1]
     
     def get_size(self):
          return self._size
     
     def is_empty(self):
          output = False
          if self.get_size() == 0:
               output = True
class TwoStacks():
     def __init__(self):
          self.stack_1 = Stack()
          self.stack_2 = Stack()
     
     def enqueue(self, content):
          for _ in range(self.stack_2.get_size()):
               temp = self.stack_2.pop()
               self.stack_1.push(temp)
          self.stack_1.push(content)
          for _ in range(self.stack_1.get_size()):
               temp = self.stack_1.pop()
               self.stack_2.push(temp)

     def dequeue(self):
          if self.stack_2.get_size() != 0:
               output = self.stack_2.pop()
          return output

     def get_size(self):
          return self.stack_2.get_size()
     
     def is_empty(self):
          output = False
          if self.get_size() == 0:
               output = True
          return output
