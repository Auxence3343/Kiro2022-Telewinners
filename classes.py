class JobClass:
    def __init__(self, job, sequence, release_date, due_date, weight):
        self.id = id
        self.sequence = sequence
        self.release_date = release_date
        self.due_date = due_date
        self.weight = weight


class TaskClass:
    def __init__(self, task, processing_time, machine):
        self.task = task
        self.processing_time = processing_time
        self.machine = machine


class MachineClass:
    def _init_(self, machine, operators):
        self.machine = machine
        self.operators = operators
