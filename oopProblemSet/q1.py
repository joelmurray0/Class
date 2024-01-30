class Trigonometry:
     def square_area(self, side):
          return side**2
     
     def rectangle_area(self, width, height):
          return width*height
     
     def triangle_area(self, width, height):
          return 0.5*width*height

shape = Trigonometry()
side = int(input("Enter the side length of square"))

rect_length = int(input("Enter the length of rectangle"))
rect_width = int(input("Enter the width of triangle"))


tri_width = int(input("Enter the length of triangle"))
tri_height = int(input("Enter the height of triangle"))

print(shape.square_area(side))
print(shape.rectangle_area(rect_width, rect_length))
print(shape.triangle_area(tri_width, tri_height))