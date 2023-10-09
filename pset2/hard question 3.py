ZODIAC_SIGN = {
     "Capricorn": 1,
     "Aquarius": 30,
     "Pisces": 60,
     "Aries": 90,
     "Taurus": 120,
     "Gemini": 151,
     "Cancer": 182,
     "Leo": 214,
     "Virgo": 245,
     "Libra": 276,
     "Scorpio": 306,
     "Sagittarius": 336
}

MONTHS = {
     "january": [1, 31],
     "february": [2, 28],
     "march": [3, 31],
     "april": [4, 30],
     "may": [5, 31],
     "june": [6, 30],
     "july": [7, 31],
     "august": [8, 31],
     "september": [9, 30],
     "october": [10, 31],
     "november": [11, 30],
     "december": [12, 31]
}

def birthday_index(month, day):
     month = MONTHS[month][0]

     x = list(MONTHS.keys())
     
     i, v = MONTHS[x[month-1]]

     sum = 10
     
     for j in range(1,i):
          sum += MONTHS[x[j-1]][1]
     
     sum = (sum + day) % 365

     return sum

def position(birth_number):
     temp = ZODIAC_SIGN
     if birth_number == 0:
          birth_number = 365
     temp["value"] = birth_number


     temp = dict(sorted(temp.items(), key = lambda x: x[1]))

     for i, v in enumerate(temp.keys()):
          if v == "value":
               pos = i
     
     if pos == 1 or pos == 0:
          print("You are a Capricorn")
     elif pos == 11:
          print("You are a Sagittarius")
     else:
          z = list(temp.keys())
          print(f"You are a {z[pos-1]}")

birthday = input("What is your birthday (month day)? \n")

month, day = birthday.split(" ")

try:
     day = int(day)
except:
     print("Invalid day")
     exit()

birth_number = birthday_index(month, day)

position(birth_number)