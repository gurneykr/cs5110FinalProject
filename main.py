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

    A_tasks = {1: 310000,
             2: 4000,
             3: 30000}
    B_tasks = {1: 300000,
             2: 3000,
             3: 41000}

    C_tasks = {1: 300000,
             2: 24000,
             3: 20000}

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

if __name__ =='__main__':
    one_agent(1000000)
    multiple_agents(3, 1000000)
    cascading_tasks(3, 1000000)
    cascading_tasks_varied_agent_ability(1000000)
    agents_and_tasks_with_type()