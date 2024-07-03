def prime_factorise(x: int):
     factors = []
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

num = input("Enter a number to be factorised into its primes. \n")

try:
     num = int(num)
except:
     print("Invalid input, enter an integer greater than or equal to 2")

if num >= 2:
     prime_factors = prime_factorise(num)

     print(f"The prime factors of {num} are:")
     for i in prime_factors:
          print(i)