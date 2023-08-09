import queue
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

def check_should_execution_proceed(process_list):
    should_execution_proceed = False
    for process in process_list:
        if process.time_left > 0:
            should_execution_proceed = True
            break
    return should_execution_proceed

def print_process_list(process_list):
    for process in process_list:
        print(vars(process))  
    print()

def print_process_table(process_list):
    table = Texttable()
    table_rows = [["process_id", "arrival_time", "burst_time", "completion_time", "turn_around_time", "wait_time", "response_time"]]
    for process in process_list:
        new_row = [process.process_id, process.arrival_time, process.burst_time, process.completion_time, process.turn_arount_time, process.wait_time, process.response_time]
        table_rows.append(new_row)
    table.add_rows(table_rows)
    table.set_max_width(200)
    print(table.draw())

def check_is_execution_completed(process_list):
    is_execution_completed = False
    for process in process_list:
        if process.time_left > 0:
            is_execution_completed = True
            break
    return is_execution_completed


if __name__ == "__main__":
    number_of_processes = input_entity("number of processes", 3, 5)
    # number_of_processes = 4
    # arrival_times = [0, 1, 2, 4]
    # burst_times = [5, 4, 2, 1]

    processes = []
    for i in range(number_of_processes):
        process_id = i + 1
        execution_time = input_entity(f'execution time of process {process_id}', 1, 10)
        # execution_time = burst_times[i]
        arrival_time = 0
        if i > 0:
            arrival_time = input_entity(f'arrival time of process {process_id}', 1, 10)
            # arrival_time = arrival_times[i]
        processes.append(Process(process_id, arrival_time, execution_time, execution_time))

    quantum_size = input_entity("quantum size", 1, 3)
    quantum_size = 2
    print({"quantum_size": quantum_size}, '\n')
    print_process_table(processes)

    ready_queue = []
    running_queue = []
    time_passed = 0

    def put_processes_in_ready_queue(processes):
        for i in range(len(processes)):
            process = processes[i]
            if process.arrival_time <= time_passed and not process.is_arrived:
                process.is_arrived = True
                ready_queue.append(process)
                print("ready_queue")
                print_process_table(ready_queue)

    put_processes_in_ready_queue(processes)

    while check_is_execution_completed(processes):
        if len(ready_queue) > 0:
            if time_passed >= ready_queue[0].arrival_time:
                ready_process = ready_queue.pop(0)
                if not ready_process.is_ready:
                    ready_process.set_response_time(time_passed)
                    ready_process.is_ready = True
                running_queue.append(ready_process)
                print("running_queue")
                print_process_table(running_queue)

            if len(running_queue) > 0:
                time_quanta = 0
                while time_quanta < quantum_size:
                    time_passed += 1
                    print(f'\n===================== time_passed {time_passed} ====================\n')
                    time_quanta += 1
                    print(f'\n===================== time_quanta {time_quanta} ====================\n')
                    running_queue[0].decrement_time_left()
                    if running_queue[0].time_left == 0:
                        break
                ran_process = running_queue.pop(0)
                put_processes_in_ready_queue(processes)
                if ran_process.time_left > 0:
                    ready_queue.append(ran_process)
                    print("ready_queue")
                    print_process_table(ready_queue)
                else: 
                    ran_process.set_completion_time(time_passed)
                    ran_process.set_turn_around_time()
                    ran_process.set_wait_time()
            else:
                time_passed += 1
                print(f'\n===================== time_passed {time_passed} ====================\n')
                put_processes_in_ready_queue(processes)
        else:
            time_passed += 1
            print(f'\n===================== time_passed {time_passed} ====================\n')
            put_processes_in_ready_queue(processes)

    print("Final Process List")
    print_process_table(processes)