def length_check(object, target):
  try:
    length = len(object)
  except TypeError:
    print("Invalid input to find length")
    output = False
  else:
    if length == target:
      output = True
  finally:
    return output
 
if length_check(input(),1) == True:
  print("Suitable length")
else:
  print("Unsuitable length")