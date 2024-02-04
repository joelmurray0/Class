class Box:
     def __init__(self, width, length, height):
          self._width = width
          self._length = length
          self._height = height

     @property
     def width(self):
          return self._width
     
     @width.setter
     def width(self, width):
          if width <= 0:
               raise ValueError("Enter a vlaid width")
          self._width = width

     @property
     def length(self):
          return self._length
     
     @length.setter
     def length(self, length):
          if length <= 0:
               raise ValueError("Enter a valid length")
          self._length = length

     @property
     def height(self):
          return self._height

     @height.setter
     def height(self, height):
          if height <= 0:
               raise ValueError("Enter a valid height")
          self._height = height
     
     def display_volume(self):
          print(self._width*self._height*self._length)
     
     def display_dimensions(self):
          print(f"{self._width}x{self._length}x{self._height}")

def main():
     width = int(input("enter width"))
     length = int(input("enter length"))
     height = int(input("enter height"))

     box = Box(width, length, height)
     box.display_volume()
     box.display_dimensions()

if __name__ == "__main__":
     main()