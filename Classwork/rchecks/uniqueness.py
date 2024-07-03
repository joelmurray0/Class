def unique_test(new_item, current_list):
  output = False
  if current_list.count(new_item) == 0:
    output = True
 
  return output

if unique_test(1, [6,1,2,3]):
  print("New")
else:
  print("Not new")