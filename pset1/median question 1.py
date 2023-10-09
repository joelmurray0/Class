def feet_to_inches(feet):
  inches = feet * 12
  print(inches)
 
def feet_to_yards(feet):
  yards = feet/3
  print(yards)
 
def feet_to_miles(feet):
  miles = feet * 0.000189394
  print(miles)
 
measurement = input("What is the measurement in feet? \n")
 
try:
  measurement = int(measurement)
except:
  print("Invalid input")
  exit()
 
feet_to_inches(measurement)
feet_to_yards(measurement)
feet_to_miles(measurement)
