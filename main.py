####################
#CS 5110 Final project

#possible ideas
#task allocation
import time

def one_agent(num_tasks):
    start_time = time.time()
    for i in range(1, num_tasks):
        i += 1

    elapsed_time = time.time() - start_time
    print("One agent time: ",elapsed_time)


def multiple_agents(num_agents, num_tasks):
    start_time = time.time()
    task_per_agent = num_tasks//num_agents

    for i in range(1, task_per_agent):
        i += 1
    elapsed_time = time.time() - start_time
    print(num_agents, "agents doing ", task_per_agent, "tasks each: ", elapsed_time)

if __name__ =='__main__':
    one_agent(1000000)
    multiple_agents(5, 1000000)