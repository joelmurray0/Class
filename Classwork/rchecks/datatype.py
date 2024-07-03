def data_type_check(object):
  return isinstance(object, str)
 
if data_type_check(1) == False:
  print("Not a string")
else:
  print("String")