def read_sum_nums(num):
  sum = 0
  for i in num:
    try:
      i = int(i)
    except:
      print("Invalid input")
      exit()
 
    sum += i
 
  print(sum)
 
num = input("Enter number \n")
 
sum = read_sum_nums(num)