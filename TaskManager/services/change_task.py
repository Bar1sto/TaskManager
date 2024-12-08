from entity import json_connect
from models.task import Task


'''Функция для редактирования задачи'''
def change_task() -> None:
    try:
        task_id = int(input('Введите ID задачи, для редактирования: '))
        title = input('Введите новое название задачи: ')
        description = input('Введите описание задачи: ')
        category = input('Укажите новую категорию задачи: ')
        due_date = input('Укажите новый срок выполнения задачи (yy-mm-dd): ')
        priority = input('Укажите новый приоритет задачи (низкий, средний, высокий): ')
        status = input('Введите новый статус задачи: ')
    except ValueError:
        print('ID должно быть числом!')
        return
    tasks = [Task(**data) for data in json_connect.Connect.load('entity/task.json')]
    for task in tasks:
        if task.task_id == task_id:
            task.title = title
            task.description = description
            task.category = category
            task.due_date = due_date
            task.priority = priority
            task.status = status
            json_connect.Connect.save('entity/task.json', tasks)
            print(f'Задача с ID {task_id} изменена успешно!')
            return
    print(f'Задача с ID {task_id} не найдена')
