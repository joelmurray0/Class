def existence_check(file):
  output = True
  try:
    temp = open(file,"r")
  except FileNotFoundError:
    output = False
  finally:
    return output
 
if existence_check("Test.txt"):
  print("File found")
else:
  print("File not found")