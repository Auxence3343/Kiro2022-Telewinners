import loadinstance
from classes import *




busyOperators = []
machines = []
operators = []


def cost(task, t): #TODO
    JobTasksId= task.job.sequence 
    Tfinal = t
    for el in JobTasksId :
        if el.task >= task.task :
            Tfinal += el.processing_time
    w = task.job.weight
    d = task.job.due_date 
    if Tfinal > d:
        arg1 = 6
    else :
        arg1 = 0
    return w(arg1 + max(Tfinal-d, 0))


def free_machines(t):
    res = []
    for m in machines:
        if m.is_free():
            res.append(m)
    return res

def free_operators(t):
    res = []
    for o in operators:
        if o.is_free(t):
            res.append(o)
    return res




def decision(time, jobs, tasks, machines, operators):
    """prend une décision à l'instant t"""
    return_sequence = []
    free_tasks = []
    free_machines = []
    free_operators = []
    
    for _ in range(len(free_tasks)):
        best_task = None
        best_cost = -1000000
        for task in free_tasks:
            cost_task = cost(task, t)
            if cost_task > best_cost:
                best_task = task
                best_cost = cost_task
        best_machine = None
        nb_operators = 10000
        for machine in free_machines:
            if machine.id in best_task.machines():
                if (len(best_task.machines[machine.id]["operators"]) < nb_operators):
                    best_machine = machine
                    nb_operators = len(machine[operators])
        
        best_operator = None
        nb_machines = 0
        for operator in free_operators:
            if operator.id in best_task.machines[best_machine.id]["operators"]:
                best_operator = operator #TO IMPROVE WHEN WE KNOW THE NB OF MACHINES
        if (best_task is not None and best_machine is not None and best_operator is not None):
            return_sequence.append((time, best_task, best_machine, best_operator))
            free_tasks.remove(best_task)
            free_machines.remove(best_machine)
            free_operators.remove(best_operator)
    return return_sequence
        

def solve(file, output):
    instance = loadinstance.load_instance(file)
    parameters = instance["parameters"]
    size = parameters["size"]
    costs = parameters["costs"]

    alpha = costs["unit_penalty"]
    beta = costs["tardiness"]
    nb_jobs = size["nb_jobs"]
    nb_tasks = size["nb_tasks"]
    nb_machines = size["nb_machines"]
    nb_operators = size["nb_operators"]

    print("The {} instance contains {} tasks in {} jobs, to complete them, we have {} machines and {} operators. "\
            .format(file, nb_tasks, nb_jobs, nb_machines, nb_operators))
    print("The tardiness penalty is {} + {} per day".format(alpha, beta))

    jobs_dict = instance["jobs"]

    for i in range(nb_machines):
        machines.append(MachineClass(i+1))
    for i in range(nb_operators):
        operators.append(OperatorClass(i+1))      


    jobs= []
    for job in jobs_dict:
        jobs.append(JobClass(job["job"], job["sequence"], job["release_date"], job["due_date"], job["weight"]))

    tasks_dict = instance["tasks"]
    tasks = []
    for task in tasks_dict:
        t = TaskClass(task['task'], task["processing_time"], task["machines"], False, None)
        tasks.append(t)


    operations_list = [] # required output

    


    for time in range(2000): #boucle temporelle
        operations_list.extend(decision(time, jobs, tasks, machines, operators))





      


solve("sujet/tiny.json", "solution/tiny.json")
solve("sujet/medium.json", "solution/medium.json")
solve("sujet/large.json", "solution/large.json")
solve("sujet/huge.json", "solution/huge.json")
