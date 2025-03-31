from classes import Task, OrderBook

if __name__ == "__main__": 
# Test Task 1 
    # t1 = Task("program hello world", "Eric", 3)
    # print(t1.id, t1.description, t1.programer, t1.workload)
    # print(t1) 
    # print(t1.is_finished())
    # t1.mark_finished()
    # print(t1)
    # print(t1.is_finished())
    # t2 = Task("program webstore", "Adele", 10)
    # t3 = Task("program mobile app for workload accounting", "Eric", 25)
    # print(t2)
    # print(t3)

# Test Task 2
    # orders = OrderBook()
    # orders.add_order("program webstore", "Adele", 10)
    # orders.add_order("program mobile app for workload accounting", "Eric", 25)
    # orders.add_order("program app for practising mathematics", "Adele", 100)
    # orders.add_order("program the next facebook","Eric",1000)

    # for order in orders.all_orders():
    #     print(order)

    # print()

    # for programmer in orders.programers():
    #     print(programmer) 

# Test Task 3 
    # print(orders.programer_tasks())

# Test Task 4 
    # orders.mark_finished(1)
    # orders.mark_finished(2)

    # for order in orders.all_orders():
    #     print(order)

    # orders.print_finished()
    # orders.print_unfinished()

# Test Task 5 
    # orders = OrderBook()
    # orders.add_order("program webstore", "Adele", 10)
    # orders.add_order("program mobile app for workload accounting", "Adele", 25)
    # orders.add_order("program app for practising mathematics", "Adele", 100)
    # orders.add_order("program the next facebook","Eric",1000)

    # orders.mark_finished(1)
    # orders.mark_finished(2)

    # status = orders.status_of_programer("Adele")
    # print(status)

# Task 6 - don't keep in memory tasks inputted beforehand, reset memory each time it is run 
    
    #while loop for "# 0:exit"

    # command
    command_id=int(input("command:"))
    arguments=[]
    software_orders=OrderBook()
    # 0: exit
    
    # 1: add order 
    if command_id==1:
        # description
        input_description=input("description: ")
        arguments.append(input_description)
        programer_and_workload=input("programer and workload estimate: ").split()
        if programer_and_workload == 2:
            # programer and workload
            input_programer=programer_and_workload[0]
            if type(input_programer)==str:
                arguments.append(input_programer)

                input_workload=int(programer_and_workload[1])
                if type(input_workload)==int:
                    arguments.append(input_workload)
                    software_orders.add_order(arguments[0],arguments[1],arguments[2])
                    print("added!")
                else:
                    raise Exception("erroneous input") 
            else:
                raise Exception("erroneous input")
        else:
            raise Exception("erroneous input")
    
    #2: list finished tasks - always outputs "[]" when there is no finished task
    elif command_id==2:
        if not software_orders.print_finished():
            print("no finished tasks")
        elif software_orders.print_finished():
            software_orders.print_finished()
        else:
            raise Exception
    
    #3: list unfinished tasks 
    elif command_id==3:
        if not software_orders.print_unfinished():
            print("no unfinished tasks")
        elif software_orders.print_unfinished():
            software_orders.print_unfinished()
        else:
            raise Exception
    
    #4: mark task as finished
    elif command_id==4:
        input_id=input("id: ")
        if type(input_id)==int and len(input_id)==1:
            if input_id in software_orders.id:
                if software_orders.status=='NOT FINISHED':
                    software_orders.mark_finished(input_id)
                    print("marked as finished")
                else:
                    raise Exception("erroneous input")
            else:
                raise Exception("erroneous input")
        else:
            raise Exception("erroneous input")

    #5: programers
    elif command_id==5:
        if not software_orders.programers():
            print("no tasks")
        elif software_orders.programers():
            software_orders.programers()
        else:
            raise Exception

    #6: status of programer 
    elif command_id==6:
        input_programer=input("programer: ")
        if input_programer in software_orders.programer:
            print(software_orders.status_of_programer(input_programer))
        else:
            raise Exception("erroneous input")

    else:
        raise Exception("Command should be included between 0 and 6")

