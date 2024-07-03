class IceCream():
     def __init__(self):
          self.list = []

     def push(self, ice_cream_flavour):
          if len(self.list) < 5:
               self.list.append(ice_cream_flavour)
          else:
               print("Max ice cream scoops given.")
     
     def pop(self):
          output = self.list[-1]
          del self.list[-1]
          return output
