#include <iostream>
#include <string>
#include <time.h>
using namespace std;
const int quantumSize = 2;
int PC;
int timer = 0;
struct process
{
    string Id;
    int IR;
    int block;
    int arrivalTime;
    int executionTime;
    int *noOfinstructions;
    int resume;
    bool isComplete;
    int *processedInstructions;
    string state;
    bool resourseNeed;
};
void init(process *p, int n)
{
    for (int i = 0; i < n; i++)
    {
        p[i].block = (i + 1) * 100;
        p[i].Id = "proc_" + to_string((i + 1) * 100);
        p[i].arrivalTime = i + 1;
        p[i].executionTime = rand() % 5 + 1;
        p[i].noOfinstructions = new int[p[i].executionTime];
        p[i].processedInstructions = new int[p[i].executionTime];
        for (int j = 0; j < p[i].executionTime; j++)
        {
            p[i].noOfinstructions[j] = (i + 1) * 100 + j + 1;
            p[i].processedInstructions[j] = -1;
        }
        p[i].IR = 0;
        p[i].resume = 0;
        p[i].isComplete = false;
        p[i].state = "Ready";
        p[i].resourseNeed = false;
    }
}

bool isProgramComplete(process *p, int n)
{
    for (int i = 0; i < n; i++)
    {
        if (p[i].isComplete == false)
        {
            return false;
        }
    }
    return true;
}
void printExecution(process *p, int i)
{
    cout << "====================================================" << endl;
    cout << endl;
    cout << "ID : " << p[i].Id << endl;
    cout << "PC :" << PC << endl;
    cout << "IR :" << p[i].IR << endl;
    cout<< "State : "<<p[i].state<<endl;
    cout << "Processed Instructions : [ ";
    for (int k = 0; k < p[i].executionTime; k++)
    {
        if (p[i].processedInstructions[k] != -1)
        {
            cout << p[i].processedInstructions[k] << " ";
        }
    }
    cout << "]";
    cout << endl;
    cout << "Remaining Instructions : [ ";
    for (int k = 0; k < p[i].executionTime; k++)
    {
        if (p[i].noOfinstructions[k] != -1)
        {
            cout << p[i].noOfinstructions[k] << " ";
        }
    }
    cout << "]";
    cout << endl;
    if (p[i].resume < p[i].executionTime)
    {

        cout << "Resume : Instruction (" << p[i].noOfinstructions[p[i].resume] << ")" << endl;
    }
    cout << "Time : " << timer << endl;
    cout << endl;
}
void runInstruction(process *p, int n)
{
    int i = 0;
    int temp = 0;
    int random;
    while (!isProgramComplete(p, n))
    {
        if (!p[i].isComplete)
        {
            PC = p[(i + 1) % n].block;
            temp = p[i].resume;
            random = rand() % 2;
            if (random == 1)
            {
                cout << "Resourse Required in process "<< endl;
                p[i].state = "block";
            }
            else
            {
                p[i].state = "ready";
            }
            if (p[i].state == "ready")
            {
                p[i].state = "running";
                for (int j = temp; j < temp + quantumSize; j++)
                {
                    if (j < p[i].executionTime)
                    {
                        p[i].IR = p[i].noOfinstructions[j];
                        p[i].processedInstructions[j] = p[i].noOfinstructions[j];
                        p[i].noOfinstructions[j] = -1;
                        p[i].resume = p[i].resume + 1;
                        timer++;
                        if (j == p[i].executionTime - 1)
                        {
                            p[i].isComplete = true;
                            break;
                        }
                    }
                }
            }
            printExecution(p, i);
            p[i].state = "ready";
        }
        i = (i + 1) % n;
    }
}
int hell(){
    return 1;
}
void checking(){
    int w,j;
    for(int i=j=5,a,b,c=b=2;i = 5;(++(++(++(++(++(i = i + 1))))))++){
        int j = (w = w+1)++;
    }
}
void print(process *p, int n)
{
    for (int i = 0; i < n; i++)
    {
        cout << "======================" << endl;
        cout << p[i].Id << endl;
        cout << "======================" << endl;
        cout << "Arrival Time :" << p[i].arrivalTime << endl;
        cout << "execution Time :" << p[i].executionTime << endl;
        cout << "IR : ins[" << p[i].IR << "]" << endl;
        cout << "Total Instructions : [ ";
        for (int j = 0; j < p[i].executionTime; j++)
        {
            cout << p[i].noOfinstructions[j] << " ";
        }
        cout << "]";
        cout << endl;
        cout << "Block : " << p[i].block << endl;
    }
}
int main()
{
    srand(time(0));
    int noOfProcess = 3;
    process *processes = new process[noOfProcess];
    init(processes, noOfProcess);
    print(processes, noOfProcess);
    cout << endl;
    cout << "Execution" << endl;
    cout << "======================" << endl;
    cout << endl;
    runInstruction(processes, noOfProcess);
    return 0;
}