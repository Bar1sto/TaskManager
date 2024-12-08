from entity import json_connect
from models.task import Task


'''Функция для добавления задачи'''
def add_task() -> None:
    title = input('Введите название задачи: ')
    description = input('Введите описание задачи: ')
    category = input('Укажите категорию задачи: ')
    due_date = input('Укажите срок выполнения задачи (yy-mm-dd): ')
    priority = input('Укажите приоритет задачи (низкий, средний, высокий): ')

    tasks = [Task(**data) for data in json_connect.Connect.load('entity/task.json')]
    task_id = max((task.task_id for task in tasks), default=0) + 1
    new_task = Task(task_id, title, description, category, due_date, priority)

    tasks.append(new_task)
    json_connect.Connect.save('entity/task.json', tasks)
    print(f'Задача "{title}" добавлена с ID: "{task_id}"')
