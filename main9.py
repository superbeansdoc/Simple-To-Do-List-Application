Checklist = []
while (True):
    Choice = int(input("Do you want to 1. Leave the program, 2. add a task or 3. remove a task"))
    if Choice == 1:
        print ("bye!")
        break
    elif Choice == 2:
        task = input("What is your task")
        Checklist.append(task)
        print("your current list!")
        print(Checklist)
    elif Choice == 3:
        lenlist = len(Checklist)
        print(Checklist)
        Remove = int(input("what would you like to remove from checklist (numbers start at 0) please chose its number"))
        if Remove <=  lenlist:
            Checklist.pop(Remove)
            print(Checklist)
        else:
            print("Thats not a number in the list try again!")
    else:
        print ("please Chose 1,2 or 3")