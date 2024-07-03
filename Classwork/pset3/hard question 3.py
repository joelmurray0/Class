def pi_to_accuracy(accuracy):
     approx = 3
     if accuracy >= 1:
          accuracy += 1
          for i in range(2, accuracy):
               starting_pos = 2 + (i - 2)*2
               term = 4/(starting_pos * (starting_pos+1) * (starting_pos+2))
               if i % 2 == 1:
                    term = -term
               approx += term

     return approx

for i in range(1, 16):
     print(f"Approximation {i}:", end="")
     print(f" {pi_to_accuracy(i)}")
