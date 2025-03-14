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

# Task 4 - finished but très lourd, moyen d'optimiser ? 
    def mark_finished(self, input_id):
        for i in range(len(self.orders)):
            if self.orders[i].id==input_id:
                self.orders[i].status="FINISHED"
            elif self.orders[i].id!=input_id:
                pass 
            else: 
                raise Exception
    
    def print_finished(self):
        finished_task=[]
        for i in range(len(self.orders)):
            if self.orders[i].status=='FINISHED':
                finished_task.append(str(self.orders[i]))
                # finished_task.append(str(self.orders[i].id) + ' : ' + self.orders[i].description)
            elif self.orders[i].status!='FINISHED':
                pass
            else:
                raise Exception
        print(finished_task)

    def print_unfinished(self):
        unfinished_task=[]
        for i in range(len(self.orders)):
            if self.orders[i].status=='NOT FINISHED':
                unfinished_task.append(str(self.orders[i]))
                # unfinished_task.append(str(self.orders[i].id) + ' : ' + self.orders[i].description)
            elif self.orders[i].status!='NOT FINISHED':
                pass
            else:
                raise Exception
        print(unfinished_task)

# Task 5 - est-ce que dans le cadre de l'exercice, je dois programmer un nouvelle fonction ? ou je peux modifier les anciens ? 
    def status_of_programer(self,input_prog):
        tasks_assigned=()
        # 1st item - number of finished tasks 
        # 2nd item - number of unfinished tasks    
        finished_counter=0
        unfinished_counter=0
        sum_finished_workload=0
        sum_unfinished_workload=0
        for i in range (len(self.orders)):
            if self.orders[i].programer==input_prog:
                if self.orders[i].status=='FINISHED':
                    finished_counter+=1
                    sum_finished_workload+=self.orders[i].workload
                elif self.orders[i].status=='NOT FINISHED':
                    unfinished_counter+=1
                    sum_unfinished_workload+=self.orders[i].workload
                else: 
                    raise Exception
            elif self.orders[i].programer!=input_prog:
                pass
            else:
                raise Exception(ValueError)
            
        tasks_assigned=(finished_counter,) + (unfinished_counter,) + (sum_finished_workload,) + (sum_unfinished_workload,) 
        
        return tasks_assigned

