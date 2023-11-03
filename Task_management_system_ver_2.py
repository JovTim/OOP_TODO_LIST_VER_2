class ToDo:
    def __init__(self, name: str, date: str):
        self.name = name
        self.date = date
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
    
    def delete_task(self, task):
        if task.due == False:
            user_warning = str(input("Are you sure you want to delete this unfinished task?(yes/no): "))
            if user_warning == "yes":
                print("Task has been deleted!")
                self.task.remove(task)
            else:
                print(f'Task has not been deleted!')
        else:
            print("Task has been deleted!")
            self.task.remove(task)


    def list_task(self):
        print(f'{self.name}:')
        for i in self.tasks:
            print(f'{i.name} - {"completed" if i.status == True else "not completed"}')

class Task:
    def __init__(self, name: str, description: str, due: str, status: bool):
        self.name = name
        self.description = description
        self.due = due
        self.status = status

    def check_task(self):
        print(f'Task Name: {self.name}\nDescription: {self.description}\nDue Date: {self.due}')
        if self.status == True:
            print(f'Task Status: Completed')
        else:
            print(f'Task Status: Not Completed')

    def edit_task(self):
        print(f'Pick to edit: \n[1]Name\n[2]Description\n[3]Due Date\n[4]Status\nEnter [end] to stop')
        while True:
            user_input = str(input("Enter number: "))
            if user_input == "1":
                name_replace = str(input("Enter new task name: "))
                self.name = name_replace
                continue
            elif user_input == "2":
                description_replace = str(input("Enter new task description: "))
                self.description = description_replace
                continue
            elif user_input == "3":
                due_replace = str(input("Enter new task due date: "))
                self.due = due_replace
                continue
            elif user_input == "4":
                original = self.status
                self.status = not original
                continue
            elif user_input == "end":
                break
            else:
                print("Incorrect Input! Please Try again")
                continue

if __name__ =="__main__":
    todo_1 = ToDo(name="House Cleaning", date="07/21/23")
    task_1 = Task(name="Clean Bedroom", description="Clean every part of the bedroom", due="07/21/23", status=False)
    task_2 = Task(name="Clean Kitchen", description="Clean every part of the kitchen", due="07/21/23", status=False)
    todo_1.add_task(task=task_1)
    todo_1.add_task(task=task_2)
    todo_1.list_task()

    todo_2 = ToDo(name="Study", date="08/11/23")
    task_3 = Task(name="Science", description="Study the anatomy lesson", due="08/12/23", status=False)
    task_4 = Task(name="Math", description="Study Fractions", due="08/12/23", status=False)

    todo_2.add_task(task_3)
    todo_2.add_task(task_4)

    todo_2.list_task()