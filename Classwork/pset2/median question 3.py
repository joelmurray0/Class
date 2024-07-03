MINS_ALLOWED = 50

def additional_mins(mins):
     left = MINS_ALLOWED
     overflow = 0

     if mins > MINS_ALLOWED:
          overflow = mins - MINS_ALLOWED
          left = 0
     else:
          left -= mins
     
     return left, overflow

def additional_texts(texts, TEXTS_ALLOWED=50):
     left = TEXTS_ALLOWED
     overflow = 0

     if texts > TEXTS_ALLOWED:
          left = 0
          overflow = texts - TEXTS_ALLOWED
     else:
          left -= texts

     return left, overflow

def mins_cost(overflow, MIN_EXTRA=0.25, PHONE_CHARGE=0.44):
     extra_cost = 0

     if overflow > 0:
          extra_cost = overflow*MIN_EXTRA
     extra_cost += PHONE_CHARGE*(MINS_ALLOWED + overflow)

     return extra_cost

def texts_cost(overflow, TEXT_EXTRA=0.15):
     extra_cost = 0

     if overflow > 0:
          extra_cost = overflow*TEXT_EXTRA
     return extra_cost

def total_cost(extra_text_cost, extra_mins_cost, BASE_CHARGE=15.00, SALES_TAX=1.05):
     total = (BASE_CHARGE + extra_mins_cost + extra_text_cost) * SALES_TAX

     return total

mins = input("What are the number of minutes used this month? \n")
texts = input("How many texts did you send this month? \n")

try:
     mins = int(mins)
     texts = int(texts)
except:
     print("Invalid input")

mins_left, over_mins = additional_mins(mins)
texts_left, over_texts = additional_texts(texts)

extra_mins_cost = mins_cost(over_mins)
extra_texts_cost = texts_cost(over_texts)

cost = total_cost(extra_texts_cost, extra_mins_cost)

print(f"The cost is £{cost:.2f}.")