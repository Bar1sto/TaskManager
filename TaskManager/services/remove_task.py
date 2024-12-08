from entity import json_connect
from models.task import Task


'''Функция для удаления задачи по ID или категории'''
def remove_task() -> None:
    print('Выберите метод удаления')
    print('1. Удаление по ID задачи')
    print('2. Удаление всех задач по категории')

    try:
        choice = int(input('Введите номер метода: '))
    except ValueError:
        print('Введите число!')
        return

    tasks = [Task(**data) for data in json_connect.Connect.load('entity/task.json')]
    if choice == 1:
        try:
            task_id = int(input('Введите ID задачи для удаления: '))
        except ValueError:
            print('ID должен быть числом')
            return
        update_task = [task for task in tasks if task.task_id != task_id]

        if len(update_task) == len(tasks):
            print(f'Задача с ID "{task_id}" не найдена')
        else:
            json_connect.Connect.save('entity/task.json', update_task)
            print(f'Задача с ID "{task_id}" была успешно удалена')
    elif choice == 2:
        category = input('Введите название категории для удаления: ').strip().lower()
        update_tasks = [task for task in tasks if task.category.lower() != category]

        if len(update_tasks) == len(tasks):
            print(f'Задачи в категории "{category}" не найдены')
        else:
            json_connect.Connect.save('entity/task.json', update_tasks)
            print(f'Все задачи категории "{category}" были удалены')
    else:
        print('Неверный выбор метода!')
