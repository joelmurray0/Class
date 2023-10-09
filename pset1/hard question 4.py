import math as m

def length_calculator(lon1, lon2, lat1, lat2, R=6371.1):
     lon1 = m.radians(lon1)
     lon2 = m.radians(lon2)
     lat1 = m.radians(lat1)
     lat2 = m.radians(lat2)

     dlon = lon2 - lon1
     dlat = lat2 - lat1

     a = m.sin(dlat / 2)**2 + m.cos(lat1) * m.cos(lat2) * m.sin(dlon / 2)**2
     c = 2 * m.atan2(m.sqrt(a), m.sqrt(1 - a))

     distance = R * c

     print(f"Distance is {distance:.2f}km")

latitude_1 = input("Enter the first latitude. \n")
longitude_1 = input("Enter the first longitude. \n")
latitude_2 = input("Enter the second latitude. \n")
longitude_2 = input("Enter the second longitude. \n")

try:
     longitude_1 = float(longitude_1)
     longitude_2 = float(longitude_2)
     latitude_1 = float(latitude_1)
     latitude_2 = float(latitude_2)
except:
     print("Invalid input")
     exit()

length_calculator(longitude_1, longitude_2, latitude_1, latitude_2)