class JobClass:
    def __init__(self, job, sequence, release_date, due_date, weight):
        self.id = id
        self.sequence = sequence
        self.release_date = release_date
        self.due_date = due_date
        self.weight = weight


class TaskClass:
    def __init__(self, task, processing_time, machines, started, end_date):
        self.task = task
        self.processing_time = processing_time
        self.machines = machines
        self.started = started
        self.end_date = end_date
        self.job = None


    def end_in_passt(self, t):
        return self.end_date < t

    def is_free(self, t, tasks):
        seq = self.job.sequence
        if self.started: 
            return False
        for i in seq:
            task2 = tasks[i-1]
            if not ( task2.started and task2.end_in_passt() ):
                return False
        return True

class MachineClass:
    def _init_(self, machine_id):
        self.machine_id = machine_id
        self.liberation_date = -1 
    def start_task(self, t, p):
        self.liberation_date = t + p
    def is_free(self, t):
        return t > self.liberation_date

class OperatorClass:
    def __init__(self, operator_id):
        self.operator_id = operator_id
        self.liberation_date = -1
    def start_task(self, t, p):
        self.liberation_date = t + p
    def is_free(self, t):
        return t > self.liberation_date
