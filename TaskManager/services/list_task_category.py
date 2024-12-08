from entity import json_connect
from models.task import Task


'''Функция для вывода списка задач по категории'''
def list_tasks_category() -> None:
    category = input('Введите категорию для фильтрации: ')
    tasks = [Task(**data) for data in json_connect.Connect.load('entity/task.json')]
    filtered_tasks = [task for task in tasks if task.category.lower() == category.lower()]

    if not filtered_tasks:
        print(f'Задачи в категории "{category}" отсутствуют!')
    else:
        for task in filtered_tasks:
            print(task)