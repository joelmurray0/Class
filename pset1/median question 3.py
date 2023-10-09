import math as m
 
def semi_perimeter(a, b, c):
  semi_perimeter = (a+b+c)/2
  return semi_perimeter
 
def area(semi_perimeter, a, b, c):
  area = m.sqrt((semi_perimeter)*(semi_perimeter - a)*(semi_perimeter - b)*(semi_perimeter - c))
  return area
 
a = input("Enter side length \n")
b = input("Enter side length \n")
c = input("Enter side length \n")
 
try:
  a = int(a)
  b = int(b)
  c = int(c)
except:
  print("Invalid input")
  exit()
 
semiperi = semi_perimeter(a, b, c)
 
print(area(semiperi, a, b, c))