import math

def display_menu():
     print(" 1. Enter radius \n 2. Display radius \n 3. Display diameter \n 4. Display area \n 5. Display perimeter \n 6. Exit")

class Circle:
     def __init__(self, radius):
          self._radius = set_radius


     def set_radius(self, radius):
          try:
               if radius <= 0:
                    raise ValueError
          except:
               raise TypeError
          self._radius = radius
     
     def get_radius(self):
          return self._radius
     
     def set_diameter(self):
          self._diameter = self._radius*2

     def get_diameter(self):
          return self._diameter
     
     def set_area(self):
          self._area = self._radius*math.pi**2

     def get_area(self):
          return self._area

     def set_perimeter(self):
          self._perimeter = 2*math.pi*self._radius

     def get_perimeter(self):
          return self._perimeter

     def display_radius(self):
          print(self.get_radius())

     def display_diameter(self):
          print(self.get_diameter())

     def display_area(self):
          print(self.get_area())

     def display_perimeter(self):
          print(self.get_perimeter())


def main():
     display_menu()
     choice = int(input("Enter choice 1-6 "))
     if choice == 1:
          rad = int(input("Enter the radius"))
          circle.set_radius(rad)
          circle.set_area()
          circle.set_diameter()
          circle.set_perimeter()
     elif choice == 2:
          circle.display_radius()
     elif choice == 3:
          circle.display_diameter()
     elif choice == 4:
          circle.display_area()
     elif choice == 5:
          circle.display_perimeter()
     else:
          exit()
          
circle = Circle()
while __name__ == "__main__":
     main()
