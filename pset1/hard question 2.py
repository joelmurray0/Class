def wind_chill(temp, speed):
     wind_chill = 35.74 + (0.6215*temp) - (35.75 * (speed**0.16)) + (0.4275*(temp)*(speed**0.16))
     print(wind_chill)

air_temp = input("What is the air temperature? \n")
wind_speed = input("What is the wind speed? \n")

try:
     air_temp = float(air_temp)
     wind_speed = float(wind_speed)
except:
     print("Invalid input")
     exit()

wind_chill(air_temp, wind_speed)
