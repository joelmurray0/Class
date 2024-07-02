import math

def display_menu():
     print(" 1. Enter radius \n 2. Display radius \n 3. Display diameter \n 4. Display area \n 5. Display perimeter \n 6. Exit")

class Circle:
     def __init__(self, radius):
          self._radius = radius

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

     def get_diameter(self):
          print(self._radius*2)

     def get_area(self):
          print(self._radius**2*math.pi)

     def get_perimeter(self):
          print(math.pi*2*self._radius)


def main():
     exit = False
     while not exit:
          display_menu()
          choice = int(input("Enter choice 1-6 "))
          if choice == 1:
               rad = int(input("Enter the radius "))
               circle = Circle(rad)
          elif choice == 2:
               print(circle._radius)
          elif choice == 3:
               circle.get_diameter()
          elif choice == 4:
               circle.get_area()
          elif choice == 5:
               circle.get_perimeter()
          else:
               exit = True


if __name__ == "__main__":
     main()