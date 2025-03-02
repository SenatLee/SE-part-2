from classes import Task, OrderBook

if __name__ == "__main__": 
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


    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Eric", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)

    # for order in orders.all_orders():
    #     print(order)

    # print()

    # for programmer in orders.programers():
    #     print(programmer) 
    
    print(orders.programer_tasks())
