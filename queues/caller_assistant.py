import random
import time
import names

class Queue:
     def __init__(self, queue, max):
          self.queue = queue
          self.max = max
          self.front_pointer = 0
          self.back_pointer = 0
          
     def enqueue(self, node):
          if len(self.queue) < self.max:
               self.queue.append(node)
               self.back_pointer += 1

     def dequeue(self):
          if self.front_pointer == self.back_pointer:
               pass
          else:
               self.front_pointer += 1
     
     def view(self):
          temp = []
          for i in range(self.back_pointer-self.front_pointer):
               temp.append(self.queue[self.front_pointer+i])
          return temp

     def get_length(self):
          return self.back_pointer - self.front_pointer
     
     def is_full(self):
          output = False
          if len(self.queue) >= self.max:
               output = True
          return output

def refresh_queue(queue):
     print("REFRESH")
     temp = queue.view()
     print(temp)
     Temp = Queue(temp, 20)
     Temp.view()
     return Temp
          

customer_queue = Queue([], 20)

assistant_status = {
     "1": 0,
     "2": 0
}

for i in range(1, random.randint(1,5)):
     customer_queue.enqueue(names.get_first_name())
customer_queue.view()

while True:
     while not customer_queue.is_full():
          print(customer_queue.view())
          if customer_queue.get_length() >= 5:
               assistant_status["3"] = 0
          else:
               try:
                    assistant_status.pop("3", None)
               except KeyError:
                    pass
          for i in range(1, len(assistant_status)+1):
               if assistant_status[f"{i}"] == 0:
                    customer_queue.dequeue()
                    assistant_status[f"{i}"] = random.randint(1,3)
               else:
                    assistant_status[f"{i}"] -= 1
          customer_queue.enqueue(names.get_first_name())
          time.sleep(1)
     print(customer_queue.view())
     customer_queue = refresh_queue(customer_queue)
     customer_queue.view()