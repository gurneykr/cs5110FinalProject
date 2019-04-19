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
            for i in range(400):
                sum += 1
            tasks_completed = tasks_completed + sum
            if tasks_completed >= num_tasks: break

        if agent2_busy == False:#do work
            agent2_busy = True
            sum = 0
            for i in range(500):
                sum += 1
            tasks_completed = tasks_completed + sum
            if tasks_completed >= num_tasks: break

        if agent3_busy == False:
            agent3_busy = True
            sum = 0
            for i in range(200):
                sum += 1
            tasks_completed = tasks_completed + sum
            if tasks_completed >= num_tasks: break

        agent1_busy = False
        agent2_busy = False
        agent3_busy = False

    elapsed_time = time.time() - start_time
    print("Cascading tasks with varied agent ability: ", elapsed_time)

def agents_and_tasks_with_type():
    agents = {1: "type A",
              2: "type B",
              3: "type A",
              4: "type C"}

    A_tasks = {1: 100,
             2: 250,
             3: 50}
    B_tasks = {1: 200,
             2: 50,
             3: 350}

    C_tasks = {1: 210,
             2: 500,
             3: 75}

    a_tasks = 0
    b_tasks = 0
    c_tasks = 0
    for agent in agents:
        if agents[agent] == 'type A':
            for task in A_tasks:
                a_tasks += A_tasks[task]

        elif agents[agent] == 'type B':
            # b_tasks = 0
            for task in B_tasks:
                b_tasks += B_tasks[task]
        elif agents[agent] == 'type C':
            # c_tasks = 0
            for task in C_tasks:
                c_tasks += C_tasks[task]

    print("a_tasks: ", a_tasks, " b_tasks: ", b_tasks, " c_tasks: ", c_tasks)

if __name__ =='__main__':
    # one_agent(1000000)
    # multiple_agents(3, 1000000)
    # cascading_tasks(3, 1000000)
    # cascading_tasks_varied_agent_ability(1000000)
    agents_and_tasks_with_type()