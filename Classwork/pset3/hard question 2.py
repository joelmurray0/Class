enough = False

def newton_root_method(x, ans):
     good = False
     guess = x/2

     if abs(guess - ans) <= 10**-12:
          good = True

     return good, guess

num = input("Enter a number you want that you want to know the approximate square root. \n")

try:
     num = float(num)
except:
     print("Invalid input")

real_result = num**(1/2)
print(real_result)
while not enough:
     enough, guess = newton_root_method(num, real_result)

     if not enough:
          num = (num + guess)/2

print(guess)

