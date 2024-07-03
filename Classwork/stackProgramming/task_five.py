class Stack():
     def __init__(self):
          self.list = []
          self._size = 0

     def push(self, content):
          self.list.append(content)
          self._size += 1
          if self.get_size() == 1:
               self.min = self.list[0]
          else:
               if content < self.min:
                    self.min = content
     
     def get_min(self):
          return self.min
          
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
          return output