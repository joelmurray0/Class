NOISE_LEVELS = {
     "jackhammer": 130,
     "Gas lawnmower": 106,
     "Alarm Clock": 70,
     "Quiet room": 40
}

def compare_noise(decibel, NOISE_LEVELS):
     temp = NOISE_LEVELS
     temp["value"] = decibel
     temp = dict(sorted(temp.items(), key = lambda x: x[1]))

     for i, v in enumerate(temp.keys()):
          if v == "value":
               pos = i

     if pos == 0:
          print("This sound is quieter than the rest of the table.")
     elif pos == 4:
          print("This sound is louder than the rest of the table.")
     else:
          z = list(temp.keys())
          print(f"This sound is in between the {z[pos-1]} and the {z[pos+1]}")

decibel = input("Enter a decibel value. \n")

try:
     decibel = float(decibel)
except:
     print("Invalid input")
     exit()

compare_noise(decibel, NOISE_LEVELS)
