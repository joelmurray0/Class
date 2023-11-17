def check_digit(code):
  sum = 0
  output = False
  for i in range(len(str(code))-1):
    sum += int(str(code)[i]) * (i + 1)
  if int(str(code[-1])) == sum % 11:
    output = True
  return output
 
if check_digit(input()):
  print("Valid")
else:
  print("Invalid")