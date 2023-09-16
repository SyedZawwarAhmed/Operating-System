from random import randint
from texttable import Texttable

class Process:
    def __init__(self, process_id, arrival_time, burst_time, execution_time):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.time_left = execution_time
        self.is_arrived = False
        self.is_ready = False
        self.completion_time = 0
        self.turn_arount_time = 0
        self.wait_time = 0
        self.response_time = 0

    def decrement_time_left(self):
        self.time_left -= 1

    def set_completion_time(self, time_passed):
        self.completion_time = time_passed

    def set_turn_around_time(self):
        self.turn_arount_time = self.completion_time - self.arrival_time

    def set_wait_time(self):
        self.wait_time = self.turn_arount_time - self.burst_time

    def set_response_time(self, time_passed):
        self.response_time = time_passed - self.arrival_time

def input_entity(entity: str, min: int, max: int):
    number_of_entities = None
    while True:
        number_of_entities = int(input(f'Enter the {entity} (min: {min}, max: {max}):- '))
        # number_of_entities = randint(0, 10)
        if number_of_entities >= min and number_of_entities <= max:
            break
    return number_of_entities

def print_process_table(process_list):
    table = Texttable()
    table_rows = [["process_id", "arrival_time", "burst_time", "completion_time", "turn_around_time", "wait_time", "response_time"]]
    for process in process_list:
        new_row = [process.process_id, process.arrival_time, process.burst_time, process.completion_time, process.turn_arount_time, process.wait_time, process.response_time]
        table_rows.append(new_row)
    table.add_rows(table_rows)
    table.set_max_width(200)
    print(table.draw())

def sort_processes_according_to_shortest_job(process_list):
    return sorted(process_list, key=lambda process: process.burst_time, reverse=False)

def sort_processes_according_to_shortest_arrival(process_list):
    return sorted(process_list, key=lambda process: process.arrival_time, reverse=False)

def get_processes_of_same_shortest_job(process_list, minimum_job):
    processes_of_same_shortest_job = []
    for process in process_list:
        if process.burst_time == minimum_job:
            processes_of_same_shortest_job.append(process)
    return processes_of_same_shortest_job

def check_should_execution_proceed(process_list):
    for process in process_list:
        if process.time_left > 0:
            return True
    return False

if __name__ == "__main__":
    number_of_processes = input_entity("number of processes", 3, 5)
    # number_of_processes = 4
    # arrival_times = [1, 2, 1, 4]
    # burst_times = [3, 4, 2, 4]
    processes = []
    for i in range(number_of_processes):
        process_id = i + 1
        arrival_time = input_entity(f'arrival time of process {process_id}', 0, 10)
        execution_time = input_entity(f'execution time of process {process_id}', 1, 10)
        # arrival_time = arrival_times[i]
        # execution_time = burst_times[i]
        processes.append(Process(process_id, arrival_time, execution_time, execution_time))

    ready_queue = []
    running_queue = []
    time_passed = 0

    print()
    while check_should_execution_proceed(processes):
        ready_queue = []
        for process in processes:
            if process.arrival_time <= time_passed and process.time_left > 0:
                ready_queue.append(process)

        if len(ready_queue) == 0:
            time_passed += 1
            print("CPU was idle when time passed is", time_passed, '\n')
        else:
            sorted_ready_queue_according_to_shortest_job = sort_processes_according_to_shortest_job(ready_queue)
            minimum_job = sorted_ready_queue_according_to_shortest_job[0].burst_time

            processes_of_same_shortest_job = get_processes_of_same_shortest_job(sorted_ready_queue_according_to_shortest_job, minimum_job)

            sorted_ready_queue_according_to_shortest_arrival = sort_processes_according_to_shortest_arrival(processes_of_same_shortest_job)
            
            running_queue = [sorted_ready_queue_according_to_shortest_arrival[0]]

            ran_process = running_queue[0]
            ran_process.set_response_time(time_passed)
            time_passed += ran_process.burst_time
            ran_process.time_left = 0
            ran_process.set_completion_time(time_passed)
            ran_process.set_turn_around_time()
            ran_process.set_wait_time()

            print("\nProcess ran when time passed is", time_passed)
            print_process_table(running_queue)
            print()

    print("Final Process Table")
    print_process_table(processes)
