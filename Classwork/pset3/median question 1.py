Continue = True
valid_input = True
list_sum = []
average = 0

def add_num(list_of_nums, new_num):
     list_of_nums.append(new_num)

     return list_of_nums

def sum_list(list_of_nums):
     sum=0

     for i in list_of_nums:
          sum += i
     
     return sum

def get_number():
     valid_input = True

     value = input("Enter a value to be added to the mean. Enter zero to end calculation. \n")

     try:
          value = float(value)
     except:
          print("Invalid input")
          valid_input = False

     if value == 0:
          valid_input = False
     
     return valid_input, value

while Continue:
     is_valid, value = get_number()
     
     if is_valid:
          list_sum = add_num(list_sum, value)
          average = sum_list(list_sum)/len(list_sum)

          print(f"Average is {average}")
     else:
          Continue = False
