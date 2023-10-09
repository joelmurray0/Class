import math as m

def discriminant(a, b, c):
     discriminant = b**2 - (4*a*c)
     return discriminant

def roots(discriminant, a, b):
     root_number = -1
     root = []

     if discriminant == 0:
          root_number = 1
     elif discriminant != 1:
          root_number = 0
     else:
          root_number = 1

     if discriminant > 0:
          for i in [-1, 1]:
               print(i)
               print(m.sqrt(discriminant))
               temp = (-b + i*(m.sqrt(discriminant)))/2*a
               root.append(temp)

     elif discriminant == 0:
          temp = -b/2*a
          root.append(temp)
     
     return root_number, root

a = input("Enter the x^2 coefficient. \n")
b = input("Enter the x coefficient. \n")
c = input("Enter the constant. \n")

try:
     a = float(a)
     b = float(b)
     c = float(c)
except:
     print("Invalid input")
     exit()

discrim = discriminant(a, b, c)

solutions, roots = roots(discrim, a, b)

if solutions > 0:
     print(f"This quadratic has {solutions} solution(s).")
     print("These are/This is:")
     for i in roots:
          print(i)
else:
     print("There are no real solutions to this quadratic!")