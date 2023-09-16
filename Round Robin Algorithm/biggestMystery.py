from random import randint

def input_entity(entity: str, min: int, max: int):
    number_of_entities = None
    while True:
        # number_of_entities = int(input(f'Enter the {entity} (min: {min}, max: {max}):- '))
        number_of_entities = randint(0, 10)
        if number_of_entities >= min and number_of_entities <= max:
            break
    return number_of_entities

def print_heading(string):
    print('========================',string,'========================')

RUNNING = "RUNNING"
BLOCK = "BLOCK"
WAITING = "WAITING"

if __name__ == "__main__":
    number_of_processes = input_entity("number of processes", 4, 4)
    processes = []
    for i in range(number_of_processes):
        process_id = i + 1
        arrival_time = input_entity(f'arrival time of process {process_id}', 0, 10)
        execution_time = input_entity(f'execution time of process {process_id}', 4, 10)
        instruction_list = [i + 1 for i in range(execution_time)]
        processes.append({"process_id": f'{chr(process_id + 64)}', "instruction_list": instruction_list, "starting_index": -1, "state": WAITING, "arrival_time": arrival_time, "burst_time": execution_time, 'resource': 0})
    quantum_size = input_entity(f'quantum size', 1, 3)
    print(quantum_size)
    print(processes)

    i = 0
    while i < len(processes):
        process = processes[i]
        if process["state"] != BLOCK:
            is_interept = input("Interrupt occur or not (y or n):- ")
            if is_interept == 'n':
                print_heading(f'PCB of {process["process_id"]}')
                print('process_id:-', process["process_id"])
                if process["starting_index"] + quantum_size <= len(process["instruction_list"]) - 1:
                    process["starting_index"] += quantum_size
                else:
                    process["starting_index"] += len(process["instruction_list"]) - process["starting_index"] - 1
                print("starting_index", process["starting_index"])
                IR = process["instruction_list"][process["starting_index"]]
                next_index = 0 if i == len(processes) - 1 else i + 1
                if process["starting_index"] < len(process["instruction_list"]) - 1:
                    PC = processes[next_index]["instruction_list"][processes[next_index]["starting_index"]+1]
                print('processor_state:- IR', IR, "PC", PC)
                process["state"] = RUNNING
                print("process_state:-", process["state"])
                if process["starting_index"] < len(process["instruction_list"]) - 1:
                    print("resume_instruction", process["instruction_list"][process["starting_index"] + 1]) 
                print("quantum_size", quantum_size)
                print("instruction_list", process["instruction_list"])
                print("arrival_time", process["arrival_time"])
                print("burst_time", process["burst_time"])
                print("resource", process["resource"])
            else:
                print_heading(f'PCB of {process["process_id"]}')
                print('process_id:-', process["process_id"])
                process["state"] = BLOCK
                print("process_state:-", process["state"])
                print("quantum_size", quantum_size)
                print("instruction_list", process["instruction_list"])
                print("arrival_time", process["arrival_time"])
                print("burst_time", process["burst_time"])
                process["resource"] = 1
                print("resource", process["resource"])
                print("starting_index", process["starting_index"])

        i += 1
        if i == len(processes):
            i = 0
