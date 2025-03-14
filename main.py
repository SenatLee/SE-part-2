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
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook","Eric",1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programer("Adele")
    print(status)

