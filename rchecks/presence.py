def presence_check(object):
  noneType = False
  if len(object) == 0:
    noneType = True
  return not noneType
 
if presence_check(input()):
  print("Input exists")
else:
  print("Nothing inputted")