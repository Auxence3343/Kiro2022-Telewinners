import loadinstance
from classes import *

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
    jobs= []
    for job in jobs_dict:
        jobs.append(JobClass(job["job"], job["sequence"], job["release_date"], job["due_date"], job["weight"]))

    tasks_dict = instance["tasks"]
    tasks = []
    for t in tasks_dict:
        tasks.append(TaskClass(t['task'], task["processing_time"], task["machine"]))
    

solve("sujet/tiny.json", "solution/tiny.json")