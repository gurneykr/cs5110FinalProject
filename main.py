####################
#CS 5110 Final project
#Krista Gurney, Janelle Miller

import time, random

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
    task_per_agent = int(num_tasks // num_agents)

    agent1_busy = False
    agent2_busy = False
    agent3_busy = False

    tasks_completed = 0
    sum = 0

    while tasks_completed < num_tasks:

        if agent1_busy == False:#do work
            agent1_busy = True
            sum = 0
            for i in range(task_per_agent):
                sum += 1
            tasks_completed = tasks_completed + sum
            if tasks_completed >= num_tasks: break

        if agent2_busy == False:#do work
            agent2_busy = True
            sum = 0
            for i in range(task_per_agent):
                sum += 1
            tasks_completed = tasks_completed + sum
            if tasks_completed >= num_tasks: break

        if agent3_busy == False:
            agent3_busy = True
            sum = 0
            for i in range(task_per_agent):
                sum += 1
            tasks_completed = tasks_completed + sum
            if tasks_completed >= num_tasks: break

        agent1_busy = False
        agent2_busy = False
        agent3_busy = False

    elapsed_time = time.time() - start_time
    print("Cascading tasks: ", elapsed_time)

def cascading_tasks_varied_agent_ability(num_tasks):
    #start with first agent, gives tasks to them
    #if agent1 is busy give tasks to agent2...

    start_time = time.time()

    agent1_busy = False
    agent2_busy = False
    agent3_busy = False

    tasks_completed = 0
    sum = 0

    while tasks_completed < num_tasks:

        if agent1_busy == False:#do work
            agent1_busy = True
            sum = 0
            for i in range(400000):
                sum += 1
            tasks_completed = tasks_completed + sum
            if tasks_completed >= num_tasks: break

        if agent2_busy == False:#do work
            agent2_busy = True
            sum = 0
            for i in range(100000):
                sum += 1
            tasks_completed = tasks_completed + sum
            if tasks_completed >= num_tasks: break

        if agent3_busy == False:
            agent3_busy = True
            sum = 0
            for i in range(500000):
                sum += 1
            tasks_completed = tasks_completed + sum
            if tasks_completed >= num_tasks: break

        agent1_busy = False
        agent2_busy = False
        agent3_busy = False

    elapsed_time = time.time() - start_time
    print("Cascading tasks with varied agent ability: ", elapsed_time)


def agents_and_tasks_with_type():
    start_time = time.time()
    agents = {1: "type A",
              2: "type B",
              3: "type A",
              4: "type C"}

    A_tasks = {1: 250000,
             2: 10000,
             3: 30000}

    B_tasks = {1: 90000,
             2: 250000,
             3: 10000}

    C_tasks = {1: 86000,
             2: 24000,
             3: 250000}

    a_tasks = 0
    b_tasks = 0
    c_tasks = 0
    for agent in agents:
        if agents[agent] == 'type A':
            for task in A_tasks:
                for i in range(A_tasks[task]):
                    a_tasks += 1

        elif agents[agent] == 'type B':
            for task in B_tasks:
                for i in range(B_tasks[task]):
                    b_tasks += 1

        elif agents[agent] == 'type C':
            for task in C_tasks:
                for i in range(C_tasks[task]):
                    c_tasks += 1

    elapsed_time = time.time() - start_time
    print("Agents and tasks with type: ", elapsed_time)

def agents_with_utility_and_task_type_random(num_tasks):
    #Randomly assigns

    agents = {1: "A", 2: "B", 3: "C", 4: "D"}
    utility = {'A': 0, 'B': 0, 'C': 0, 'D':0 }

    taskTypes = ['A', 'B', 'C', 'D']
    tasks = []
    currentTask = 0
    work = 0

    for i in range(num_tasks):
        tasks.append(random.choice(taskTypes))

    start_time = time.time()

    while currentTask < num_tasks:

        for agent in agents:
            if agents[agent] == tasks[currentTask]:
                utility[agents.get(agent)] += 1
            currentTask += 1
            work += 1

    elapsed_time = time.time() - start_time
    print("Randomly allocating tasks with type to agents with utility: ", elapsed_time)
    print("\tAgent A's Utility: ", utility['A'], "\tAgent B's Utility: ", utility['B'])
    print("\tAgent C's Utility: ", utility['C'], "\tAgent D's Utility: ", utility['D'],'\n')

def agents_with_utility_and_task_type_centralized(num_tasks):
    #Randomly assigns

    agents = {1: "A", 2: "B", 3: "C", 4: "D"}
    utility = {'A': 0, 'B': 0, 'C': 0, 'D':0 }

    taskTypes = ['A', 'B', 'C', 'D']
    tasks = []
    currentTask = 0

    work = 0

    for i in range(num_tasks):
        tasks.append(random.choice(taskTypes))

    start_time = time.time()

    for task in tasks:
        if task == 'A':
            utility['A'] += 1
            work += 1
        elif task == 'B':
            utility['B'] += 1
            work += 1
        elif task == 'C':
            utility['C'] += 1
            work += 1
        elif task == 'D':
            utility['D'] += 1
            work += 1

    elapsed_time = time.time() - start_time
    print("Allocating preferred tasks with type to agents with utility: ", elapsed_time)
    print("\tAgent A's Utility: ", utility['A'], "\tAgent B's Utility: ", utility['B'])
    print("\tAgent C's Utility: ", utility['C'], "\tAgent D's Utility: ", utility['D'],'\n')

def agents_in_coalitions():
    # TODO
    start_time = time.time()



if __name__ =='__main__':
    TASKS = 1000000
    one_agent(TASKS)
    multiple_agents(3, TASKS)
    cascading_tasks(3, TASKS)
    cascading_tasks_varied_agent_ability(TASKS)
    agents_and_tasks_with_type()
    agents_with_utility_and_task_type_random(TASKS)
    agents_with_utility_and_task_type_centralized(TASKS)