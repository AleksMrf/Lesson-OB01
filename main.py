class Task:
    def __init__(self):
        self.tasks = []

    def addition_task(self, period, description):
        self.tasks.append({'period': period, 'description': description,
                           'status': "не выполнено"})

    def complete_tasks(self, description):
        found = False
        for task in self.tasks:
            if task['description'] == description:
                task['status'] = "Выполнено"
                print(f"Задача {description} выполнена")
                found = True
                break
        if not found:
            print(f"Задача {description} не найдена")

    def show_tasks(self):
        print("Текущие задачи:")
        for task in self.tasks:
            print(f"{task['description']} - {task['period']} - {task['status']}")

t = Task()
t.addition_task("9:00", "Поесть")
t.addition_task("10:00", "Позаниматься")
t.addition_task("23:45", "Поспать")

t.show_tasks()



