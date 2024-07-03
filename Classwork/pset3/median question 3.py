import random as r

HEADS = "H"
TAILS = "T"
throws = []
met = False

def toss(tosses = []):
     if r.randint(0,1) == 1:
          tosses.append(HEADS)
     else:
          tosses.append(TAILS)

     if len(tosses) != 1:
          print()
     print("So far:")

     for i in range(len(tosses)):
          if i != len(tosses)-1:
               print(f"{tosses[i]}, ", end="")
          else:
               print(tosses[-1], end="")


     return tosses

def check_row(tosses):
     flag = False

     if tosses[-1] == tosses[-2] == tosses[-3]:
          flag = True

     return flag

for _ in range(3):
     throws = toss(throws)

met = check_row(throws)

while met == False:
     throws = toss(throws)
     met = check_row(throws)

print(f" ({len(throws)} flips)")


