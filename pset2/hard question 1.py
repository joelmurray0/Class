BOARD_LENGTH = 8
flag = True

x_dict = {
     "a": 1,
     "b": 2,
     "c": 3,
     "d": 4,
     "e": 5,
     "f": 6,
     "g": 7,
     "h": 8,
}

def check_black(x, y, x_dict):
     black = False
     x = x_dict[x]
     total = x + y

     if total % 2 == 0:
          black = True

     return black


coord = input("Enter the coordinate \n")

x = coord[0]
y = coord[1]

try:
     y = int(y)
except:
     flag = False

if not ((97 <= ord(x.lower()) <= 104) and (1 <= y <= BOARD_LENGTH)):
     flag = False

if flag == False:
     print("Invalid input")
     exit()


if check_black(x, y, x_dict) == True:
     print("You are on a black square")
else:
     print("You are on a white square")