import math as m

def final_speed(height, initial_speed = 0, gravity= 9.81):
     final_speed = m.sqrt((initial_speed**2)+2*gravity*height)
     print(final_speed)

height = input("How high is the object dropped from? \n")

try:
     height = float(height)
except:
     print("Invalid input")
     exit()

final_speed(height)