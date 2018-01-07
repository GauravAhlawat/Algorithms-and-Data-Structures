import queue
import random

class Printer:
    def __init__(self, page_per_minute):
        self.pagerate = page_per_minute
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task != None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages()*60/self.pagerate


class Task:
    def __init__(self, time):
        self.time_stamp = time
        self.pages = random.randrange(1,21)

    def get_stamp(self):
        return self.time_stamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.time_stamp

def printer_simulation(num_seconds, pages_per_minute):

    lab_printer = Printer(pages_per_minute)
    print_queue = queue()
    waiting_time = []

    for current_second in range(num_seconds):
        if new_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)

        if (not lab_printer.busy()) and (not print_queue.isEmpty()):
            next_task = print_queue.deque()
            waiting_time.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)
        lab_printer.tick()

    average_wait = sum(waiting_time)/ len(wait_time)
    print('Average wait %6.2f seconds and %3d tasks still remaining' %(average_wait, print_queue.size()))



def new_print_task():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

for i in range(10):
    simulation(3600,5)

for i in range(10):
    simulation(3600,10)
