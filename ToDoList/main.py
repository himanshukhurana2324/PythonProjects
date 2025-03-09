userPromptMain = "Type Add, Show, Edit or Exit: "
userPrompt = "Enter the Task: "
tasks = []

while True:

    command = input(userPromptMain).strip().lower()

    if command == "add":
        task = input(userPrompt)
        tasks.append(task)

    elif command == "show":
        for x in range(len(tasks)):
            print(str(x+1) + ": " +tasks[x])
        
    elif command == "edit":

        for x in range(len(tasks)):
            print(str(x+1) + ": " +tasks[x])

        tno = int(input("Enter the Task number to edit: "))
        newTask= input("Enter the new task: ")
        tasks[tno-1]= newTask.strip().title()    

    elif command == "exit":
        break

    else:
        print("Invalid command. Please try again.")
