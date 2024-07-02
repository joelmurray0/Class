class Cube:
     def __init__(self, edge):
          self.edge = edge
     
     @property
     def edge(self):
          return self._edge
     
     @edge.setter
     def edge(self, edge):
          if edge <= 0:
               raise ValueError("Enter a valid edge length")
          self._edge = edge

     def display_volume(self):
          return self._edge**3
     
     def display_one_surface(self):
          return self._edge**2
     
     def display_total_surface(self):
          return 6*self.display_one_surface()
     
edge = int(input("Enter the length of the edge."))
cube = Cube(edge)
print(cube.display_volume(), cube.display_one_surface(), cube.display_total_surface())