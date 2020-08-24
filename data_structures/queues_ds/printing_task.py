from data_structures.queues_ds.queue import Queue
from data_structures.queues_ds.printer import Printer
from data_structures.queues_ds.task import Task
import random


def simulation(num_of_seconds, pages_per_minutes):
    lab_printer = Printer(pages_per_minutes)
    print_queue = Queue()
    waiting_time = []

    for current_second in range(num_of_seconds):

        if new_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)

        if (not lab_printer.in_use()) and (not print_queue.isEmpty()):
            next_task = print_queue.dequeue()
            waiting_time.append(next_task.wait_time(current_second))
            lab_printer.start_task(next_task)

        lab_printer.timer()

    average_wait = sum(waiting_time) / len(waiting_time)
    print(f"Average Wait {average_wait} secs {print_queue.size()} tasks "
          f"remaining.")


def new_print_task():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


for i in range(10):
    print(simulation(3600, 10))
