class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Задача "{task}" добавлена в список.')

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f'Задача "{task}" удалена из списка.')
        else:
            print(f'Задачи "{task}" нет в списке.')

    def view_tasks(self):
        if self.tasks:
            print("Список задач:")
            for index, task in enumerate(self.tasks, start=1):
                print(f'{index}. {task}')
        else:
            print("Список задач пуст.")

    def clear_tasks(self):
        self.tasks = []
        print("Список задач очищен.")

    def save_tasks_to_file(self, file_name):
        with open(file_name, 'w', encoding="UTF-8") as file:
            for task in self.tasks:
                file.write(f'{task}\n')
        print(f'Задачи сохранены в файл {file_name}.')

    def load_tasks_from_file(self, file_name):
        try:
            with open(file_name, 'r', encoding="UTF-8") as file:
                lines = file.readlines()
                self.tasks = [line.strip() for line in lines]
            print(f'Задачи загружены из файла {file_name}.')
        except FileNotFoundError:
            print(f'Файл {file_name} не найден.')

# Пример использования:

task_list = TaskList()

# Загрузка задач из файла
task_list.load_tasks_from_file("tasks.txt")

# Просмотр загруженных задач
task_list.view_tasks()

# Добавление новых задач
task_list.add_task("Погладить кота")
task_list.add_task("Сделать покупки")
task_list.add_task("Выучить Python")

# Сохранение задач в файл
task_list.save_tasks_to_file("tasks.txt")

# Просмотр задач после добавления и сохранения
task_list.view_tasks()
