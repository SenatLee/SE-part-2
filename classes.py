# Task 1 
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

# Task 2 
class OrderBook(object):
    def __init__(self):
        self.orders = []
        
    def add_order(self, description, programer, workload, status = "NOT FINISHED"):
        self.orders.append(Task(description, programer, workload, status)) 

    def all_orders(self):
        od = []
        for i in range(len(self.orders)):
            od.append(self.orders[i])
        return od

    def programers(self):
        prog = set()
        for i in range(len(self.orders)): 
            prog.add(self.orders[i].programer)
        return prog
    
# Task 3 
    def programer_tasks(self):
        prog_task={}
        for i in range(len(self.orders)):
            if self.orders[i].programer in prog_task:
                prog_task[self.orders[i].programer].append(self.orders[i].id)

            elif self.orders[i].programer not in prog_task:
                prog_task[self.orders[i].programer] = [self.orders[i].id]     
            else:
                raise Exception #add exception msg 
        return prog_task

# Task 4 
    def mark_finished(self, input_id):
        #need to enter inside self.orders to get the Task instance for which the id = input_id and then change its status to finished 
        self.orders[input_id].status="FINISHED"
