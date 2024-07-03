import math as m
 
def circle_area(radius):
  area = (radius**2) * m.pi
  print(area)
 
def sphere_volume(radius):
  volume = (4/3)* (radius**3) * m.pi
  print(volume)
 
radius = input("Enter the radius \n")
 
try:
  radius = int(radius)
except:
  print("Invalid input")
  exit()
 
circle_area(radius)
sphere_volume(radius)