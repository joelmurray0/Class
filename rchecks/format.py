def format_check(object):
  valid = False
  try:
    object = object.split("/")
    if length_check(object[0],2) and length_check(object[1],2) and length_check(object[2],4):
      valid = True
  except TypeError:
    pass
  finally:
    return valid
 
if format_check(input("Enter date in dd/mm/yyyy format: ")):
  print("Valid date")
else:
  print("Invalid input to format check")