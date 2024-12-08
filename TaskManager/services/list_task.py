from entity import json_connect

'''Функция для вывода списка всех задач'''
def list_task() -> None:
    tasks = json_connect.Connect.load('entity/task.json')
    if not tasks:
        print('Задачи отсутствуют!')
    else:
        for task in tasks:
            print(task)
