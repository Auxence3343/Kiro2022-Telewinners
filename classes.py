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
