class Task(object): 
    id=1
    def __init__(self, description, programer, workload, status = "NOT FINISHED"):
        self.description = description
        self.workload = workload
        self.programer = programer
        self.status = status
        self.id=type(self).id
        type(self).id += 1

    def is_finished(self):
        if self.status == "NOT FINISHED":
            return False 
        elif self.status == "FINISHED":
            return True
        else:
            raise Exception #add exception msg 

    def mark_finished(self):
        self.status="FINISHED"

    def __str__(self):
        return "{0}: {1} ({2} hours), programer {3} {4}".format(self.id, self.description, self.workload, self.programer, self.status)

class OrderBook(object):
    def __init__(self):
        self.orders = []
        
    def add_order(self, description, programer, workload, status = "NOT FINISHED"):
        self.orders.append(Task(description, programer, workload, status)) 

    def all_orders(self):
        tasks = []
        tasks.append(self)    
        return tasks

    def programers(self):
        prog = []
        if self.programer not in prog:
            prog.append(self.programer)
        elif self.programer not in prog:
            prog = prog
        else:
            raise Exception #add exception msg
        return prog 
    
