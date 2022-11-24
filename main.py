import loadinstance

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

    jobs = instance["jobs"]

solve("sujet/tiny.json", "solution/tiny.json")