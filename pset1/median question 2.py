import math as m
 
def base_area(radius):
  area = m.pi * (radius**2)
  return area
 
radius = input("What is the radius? \n")
height = input("What is the height? \n")
 
try:
  radius = int(radius)
  height = int(height)
except:
  print("Invalid input")
  exit()
 
circle_area = base_area(radius)
print(f"Area is {height * circle_area}")