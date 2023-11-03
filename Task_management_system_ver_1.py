class Tasks:
    def __init__(self, name: str, description: str, due: str, status: bool):
        self.name = name
        self.description = description
        self.due = due
        self.status = status
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self):
        if self.status == False:
            user_warning = str(input("Are you sure you want to delete this unfinished task?(yes/no): "))
            if user_warning == 'yes':
                print('Task has been deleted!')
                del self
            else:
                print("Task is not deleted!")
        else:
            print('Task has been deleted!')
        

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


if __name__=="__main__":
    task_1 = Tasks(name="Clean Bedroom", description="Clean your bedroom", due="tomorrow", status=False)
    task_1.delete_task()