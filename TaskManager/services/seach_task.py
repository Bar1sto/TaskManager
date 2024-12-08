from entity import json_connect
from models.task import Task


'''Функция для поиска задачи по ключевому слову'''
def search_tasks() -> None:
    keyword = input('Введите ключевое слово для поиска: ').lower()
    tasks = [Task(**data) for data in json_connect.Connect.load('entity/task.json')]
    matching_tasks = [
        task for task in tasks
        if keyword in task.title.lower() or keyword in task.description.lower()
    ]

    if not matching_tasks:
        print(f'Задачи, содержащие "{keyword}", не найдены!')
    else:
        for task in matching_tasks:
            print(task)
