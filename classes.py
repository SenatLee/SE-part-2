class Task(object): 
    id=1
    def __init__(self, description, programmer, workload, status = "NOT FINISHED"):
        self.description = description
        self.workload = workload
        self.programmer = programmer
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
        return self.id + " : " + self.description + "(" + self.workload + "hours), " + "programmer" + self.programmer + self.status
        # return "{0}: {1} ({2} hours), programmer {3} {4}".format(self.id, self.description, self.workload, self.programmer, self.status)

class OrderBook(Task):
        
    def add_order(self, description, programmer, workload, status = "NOT FINISHED"):
        super().__init__(description, programmer, workload, status) 

    def all_orders(self):
        tasks = []
        tasks.append(self)    
        return tasks

    def programmers(self):
        prog = []
        if self.programmer not in prog:
            prog.append(self.programmer)
        elif self.programmer not in prog:
            prog = prog
        else:
            raise Exception #add exception msg
        return prog