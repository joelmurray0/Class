class Clock(object):
     def __init__(self, time):
          self.time = time

     def print_time(self):
          print(self.time)

b_c = Clock("5:30")
p_c = b_c
p_c.time = "10:30"
b_c.print_time()