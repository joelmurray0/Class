NUMBER_WORDS = {
     "one": 1,
     "two": 2,
     "three": 3,
     "four": 4,
     "five": 5,
     "six": 6,
     "seven": 7,
     "eight": 8,
     "nine": 9,
     "zero": 0,
}

def numbers_find(string):
     LENGTH = len(string)
     nums = "1234567890"
     first_num = ""
     counter = 0

     passed = False
     while not passed:
          if string[counter] in nums:
               first_num = string[counter]
               passed = True
          counter += 1
          if counter > LENGTH:
               return 0
     passed = False
     counter = 1
     second_num = ""
     while not passed:
          if string[-counter] in nums:
               passed = True
               second_num = string[-counter]
          counter += 1
     return int(first_num + second_num)


sum = 0
# The text file was removed - the code works though!
with open("codingAdvent\problem1.txt", "r")as file:
     inputs = file.readlines()
     
for i in inputs:
     sum += numbers_find(i,NUMBER_WORDS)
print(sum)
