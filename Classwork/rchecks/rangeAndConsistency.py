def range_check(int, min, max):
  within = False
  if min <= int <= max:
    within = True
  return within

def consistency_check(month):
  output = False
  if range_check(month, 1, 12):
    output = True
  return output
 
if consistency_check(int(input())):
  print("Valid month")
else:
  print("Invalid month")
 
if range_check(2,1,3) == True:
  print("Within range")
else:
  print("Outside of range")