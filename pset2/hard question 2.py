ELECTROMAGNETIC_SPECTRUM = {
     "Radio Waves": 0,
     "Microwaves": 3*(10**9),
     "Infrared light":3* (10**12),
     "Visible light": 4.3* (10**14),
     "Ultraviolet light":7.5* (10**14),
     "X-rays": 3* (10**17),
     "Gamma rays": 3* (10**19)
}

def range(frequency):
     temp = ELECTROMAGNETIC_SPECTRUM
     temp["value"] = frequency
     temp = dict(sorted(temp.items(), key = lambda x: x[1]))

     for i, v in enumerate(temp.keys()):
          if v == "value":
               pos = i
     
     if pos == 0:
          print("Type of wave: Radio wave.")
     elif pos == 7:
          print("Type of wave: Gamma ray.")
     else:
          z = list(temp.keys())
          print(f"Type of wave: {z[pos-1]}")


frequency = input("Enter the frequency. \n")

try:
     frequency = float(frequency)
except:
     print("Invalid input")
     exit()

range(frequency)