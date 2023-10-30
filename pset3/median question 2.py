def prime_factorise(x: int):
     factors = [1]
     n = 2

     while n**2 <= x:
          if x % n == 0:
               factors.append(n)
               x //= n
          else:
               n += 1
     if x > 1:
          factors.append(x)

     return factors


def lcm(x_fact: list, y_fact: list):
     lcm = 1
     shared_factors = []

     x_fact.sort()
     y_fact.sort()

     if len(x_fact) < len(y_fact):
          for i in range (len(x_fact)):
               if x_fact[i] == y_fact[i]:
                    shared_factors.append(x_fact[i])
     else:
          for i in range (len(y_fact)):
               if y_fact[i] == x_fact[i]:
                    shared_factors.append(y_fact[i])

     for factor in shared_factors:
          lcm *= factor

     return lcm

num1 = input("Enter a number \n")
num2 = input("Enter a second number \n")

try:
     num1 = int(num1)
     num2 = int(num2)
except:
     print("Please only enter integers.")

x = prime_factorise(num1)
y = prime_factorise(num2)


ans = lcm(x,y)

print(f"The lcm of {num1} and {num2} is: {ans}")