userPromptMain = "Type Add, Show, Edit, Complete or Exit: "
userPrompt = "Enter the Task: "
tasks = []

while True:

    command = input(userPromptMain).strip().lower()

    if command == "add":
        task = input(userPrompt)+"\n"
         
        file= open("ToDoList/tasks.txt", 'a+')
        file.writelines(task)
        file.close()

    elif command == "show":

        tasks= open("ToDoList/tasks.txt", 'r').readlines()
        for index, t in enumerate(tasks):
            print(f"{index+1}-{t}", end='')
        
    elif command == "edit":

        for index, t in enumerate(tasks):
            print(f"{index+1}-{t}")

        tno = int(input("Enter the Task number to edit: "))
        newTask= input("Enter the new task: ")
        tasks[tno-1]= newTask.strip().title()     

    elif command == "exit":
        break

    elif command=="complete":
        for index, t in enumerate(tasks):
            print(f"{index+1}-{t}")

        tno = int(input("Enter the Task number completed: "))
        tasks.pop(tno-1)

    else:
        print("Invalid command. Please try again.")
