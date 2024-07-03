HOLIDAYS = {
     "Jan 1": "New Year's Day",
     "July 1": "Canada Day",
     "Dec 25": "Christmas Day"
}

MONTHS = {
     "january": "Jan",
     "february": "Feb",
     "march": "March",
     "april": "April",
     "may": "May",
     "june": "June",
     "july": "July",
     "august": "Aug",
     "september": "Sep",
     "october": "Oct",
     "november": "Nov",
     "december": "Dec"
}

def make_string(day, month, MONTHS):
     str_day = str(day)
     str_month = MONTHS[month.lower()]

     return str_month + " " + str_day

def compare(date, HOLIDAYS):
     for day in HOLIDAYS:
          if day == date:
               print(HOLIDAYS[date])

month = input("Enter a month. \n")
day = input("Enter a day. \n")

try:
     day = int(day)
except:
     print("Invalid day input")
     exit()

date = make_string(day,month, MONTHS)

compare(date, HOLIDAYS)