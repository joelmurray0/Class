MONTHS = {
     "january": 31,
     "february": 28,
     "march": 31,
     "april": 30,
     "may": 31,
     "june": 30,
     "july": 31,
     "august": 31,
     "september": 30,
     "october": 31,
     "november": 30,
     "december": 31
}

def date_successor(day, month, year):
     new_day = 0
     new_month = ""
     new_year = 0
     
     list_of_months = list(MONTHS.keys())

     if MONTHS[month] == day:
          index = list_of_months.index(month) + 1

          if index == 12:
               new_month = "january"
          else:     
               new_month = list_of_months[index]

          new_day = 1

          if new_month == "january":
               new_year = year + 1
          else:
               new_year = year
     else:
          new_day = day + 1
          new_month = month
          new_year = year
     
     return new_day, new_month, new_year

day = input("What day is it? (day month year)\n")

day, month, year = day.split(" ")

try:
     day = int(day)
     year = int(year)
except:
     print("Invalid input. Remember to put in the form day month year all spaced.")

day_s, month_s, year_s = date_successor(day, month, year)

print(f"{day_s} {month_s} {year_s}")