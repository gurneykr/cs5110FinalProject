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


def cascading_tasks(num_agents, num_tasks):
    #start with first agent, gives tasks to them
    #if agent1 is busy give tasks to agent2...

    start_time = time.time()
    task_per_agent = num_tasks // num_agents

    agent1_busy = False
    agent2_busy = False
    agent3_busy = False

    tasks_completed = 0
    sum = 0

    while tasks_completed < num_tasks:

        if agent1_busy == False:#do work
            agent1_busy = True
            sum = 0
            for i in range(task_per_agent//2):
                sum += 1
            tasks_completed = tasks_completed + sum
            if tasks_completed >= num_tasks: break

        if agent2_busy == False:#do work
            agent2_busy = True
            sum = 0
            for i in range(task_per_agent//2):
                sum += 1
            tasks_completed = tasks_completed + sum
            if tasks_completed >= num_tasks: break

        if agent3_busy == False:
            agent3_busy = True
            sum = 0
            for i in range(task_per_agent//2):
                sum += 1
            tasks_completed = tasks_completed + sum
            if tasks_completed >= num_tasks: break

        agent1_busy = False
        agent2_busy = False
        agent3_busy = False

    elapsed_time = time.time() - start_time
    print("Cascading tasks: ", elapsed_time)

if __name__ =='__main__':
    one_agent(1000000)
    multiple_agents(3, 1000000)
    cascading_tasks(3, 1000000)