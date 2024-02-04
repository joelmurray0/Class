import math

def display_menu():
     print(" 1. Enter radius \n 2. Display radius \n 3. Display diameter \n 4. Display area \n 5. Display perimeter \n 6. Exit")

class Circle:
     def __init__(self, radius):
          self._radius = radius
          self._diameter = radius*2
          self._perimeter = radius*2*math.pi
          self._area = radius*math.pi**2

     @property
     def diameter(self):
          return self._diameter
     
     @diameter.setter
     def diameter(self, radius):
          self._diameter = radius*2

     @property
     def radius(self):
          if not self._radius:
               raise ValueError("Input a radius first")
          return self._radius
     
     @radius.setter
     def radius(self, radius):
          try:
               if radius <= 0:
                    raise ValueError
          except:
               raise TypeError
          self._radius = radius
     
     @property
     def area(self):
          return self._area
     
     @area.setter
     def area(self, radius):
          self._area = radius*math.pi**2

     @property
     def perimeter(self):
          return self._perimeter

     @perimeter.setter
     def perimeter(self, radius):
          self._perimeter = 2*math.pi*radius

     def display_radius(self):
          print(self.radius)

     def display_diameter(self):
          print(self._diameter)

     def display_area(self):
          print(self._area)

     def display_perimeter(self):
          print(self._perimeter)


def main():
     exit = False
     while not exit:
          display_menu()
          choice = int(input("Enter choice 1-6 "))
          if choice == 1:
               rad = int(input("Enter the radius "))
               circle = Circle(rad)
          elif choice == 2:
               circle.display_radius()
          elif choice == 3:
               circle.display_diameter()
          elif choice == 4:
               circle.display_area()
          elif choice == 5:
               circle.display_perimeter()
          else:
               exit = True


if __name__ == "__main__":
     main()