class Box:
     def __init__(self, width, length, height):
          self._width = width
          self._length = length
          self._height = height

     def display_volume(self):
          print(self._width*self._height*self._length)
     
     def display_dimensions(self):
          print(f"{self._width}x{self._length}x{self._height}")



width = int(input("enter width"))
length = int(input("enter length"))
height = int(input("enter height"))

box = Box(width, length, height)
box.display_volume()
box.display_dimensions()