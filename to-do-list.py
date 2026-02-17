data=[]

while True:
    print("==== To-Do List Menu ====")
    print('''Operation
    1. Show task
    2. Add  task
    3. Update task
    4. Delete task
    5. Exits''')
    
    operation=input("Choose Operations (1/2/3/4/5) : ")
    
    #show task 
    if operation=="1":
        if not data:
            print("No task found.\n")
        else:
            print("\nYour To-Do List:")
            for idx , task  in enumerate(data, start=1):
                print(f"{idx}. {task}")         
        
    #add task
    elif operation=="2":
        put=input("enter the task: ")
        data.append(put)
        print(f"'{put}' data inserted succefully\n")
      
    # Update task
    elif operation=="3":
        if not data:
            print("No task updated.")
        else:
            for idx,task in enumerate(data, start=1):
                print(f"{idx}. {task}")
            try:
                update=int(input("Enter the task number to Update : "))
                if 1 <= update <= len(data):
                    new_data=input("enter new data : ")   
                    data[update - 1] = new_data
                    print("Task updated successfully!\n")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.\n")

    # task delete
    elif operation=="4":
        print("Your To-Do list")
        if not data:
            print("No task deleted.")
        else:
            for idx,task in enumerate(data, start=1):
                print(f"{idx}. {task}")
            try:
                delete=int(input("Enter the task number to delete : "))
                if 1 <= delete <= len(data):
                    removed_task=data.pop(delete - 1)
                    print(f"Task '{removed_task}' deleted successfully!\n")
            except ValueError:
                print("Please enter a valid number.")
    
    # Exit
    elif operation=="5":
        print("Exiting the To-Do List application!\n")
        break
    else:
        print("Invalid choice. Please select 1-5.\n")


                

        





 