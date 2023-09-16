import random

class Process:
    def __init__(self, n):
        self.Id = f"proc_{n * 100}"
        self.IR = 0
        self.block = (n + 1) * 100
        self.arrivalTime = n + 1
        self.executionTime = random.randint(1, 5)
        self.noOfinstructions = [n * 100 + j + 1 for j in range(self.executionTime)]
        self.processedInstructions = [-1] * self.executionTime
        self.resume = 0
        self.isComplete = False
        self.state = "Ready"
        self.resourseNeed = False

def init(processes, n):
    for i in range(n):
        processes[i] = Process(i)
        
def is_program_complete(processes, n):
    return all(not p.isComplete for p in processes)

def print_execution(p, i, PC, timer):
    print("====================================================")
    print()
    print(f"ID : {p.Id}")
    print(f"PC : {PC}")
    print(f"IR : {p.IR}")
    print(f"State : {p.state}")
    
    processed_instructions = [instr for instr in p.processedInstructions if instr != -1]
    print("Processed Instructions :", processed_instructions)
    
    remaining_instructions = [instr for instr in p.noOfinstructions if instr != -1]
    print("Remaining Instructions :", remaining_instructions)
    
    if p.resume < p.executionTime:
        print(f"Resume : Instruction ({p.noOfinstructions[p.resume]})")
    print(f"Time : {timer}")
    print()

def run_instruction(processes, n):
    PC = 0
    timer = 0
    i = 0
    
    while not is_program_complete(processes, n):
        if not processes[i].isComplete:
            PC = processes[(i + 1) % n].block
            temp = processes[i].resume
            random_val = random.randint(0, 1)
            
            if random_val == 1:
                print("Resource Required in process")
                processes[i].state = "block"
            else:
                processes[i].state = "ready"
                
            if processes[i].state == "ready":
                processes[i].state = "running"
                for j in range(temp, temp + quantumSize):
                    if j < processes[i].executionTime:
                        processes[i].IR = processes[i].noOfinstructions[j]
                        processes[i].processedInstructions[j] = processes[i].noOfinstructions[j]
                        processes[i].noOfinstructions[j] = -1
                        processes[i].resume = processes[i].resume + 1
                        timer += 1
                        if j == processes[i].executionTime - 1:
                            processes[i].isComplete = True
                            break
                print_execution(processes[i], i, PC, timer)
                processes[i].state = "ready"
        i = (i + 1) % n

def main():
    random.seed()
    no_of_processes = 3
    processes = [None] * no_of_processes
    init(processes, no_of_processes)
    
    for p in processes:
        print("======================")
        print(p.Id)
        print("======================")
        print(f"Arrival Time : {p.arrivalTime}")
        print(f"Execution Time : {p.executionTime}")
        print(f"IR : ins[{p.IR}]")
        print("Total Instructions :", p.noOfinstructions)
        print(f"Block : {p.block}")
    
    print()
    print("Execution")
    print("======================")
    print()
    run_instruction(processes, no_of_processes)

if __name__ == "__main__":
    main()
