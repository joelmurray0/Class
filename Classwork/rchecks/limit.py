def limit_check(int, bound):
  above = True
  if int < bound:
    above = False
  return above
 
if limit_check(2,1) == True:
  print("Above limit")
else:
  print("Below limit")