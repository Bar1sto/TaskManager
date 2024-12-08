from services.add_task import add_task
from services.remove_task import remove_task
from services.seach_task import search_tasks
from services.list_task_category import list_tasks_category
from services.list_task import list_task
from services.change_task import change_task

'''
Главная функция
'''
def main():
    while True:
        print('Выбор:')
        print('1. Добавить задачу')
        print('2. Удалить задачу')
        print('3. Редактировать задачу')
        print('4. Просмотреть все задачи')
        print('5. Просмотреть задачи по категории')
        print('6. Найти задачи по ключевым словам')
        print('7. Выйти из программы')

        try:
            action = int(input('Введите номер действия: '))
        except ValueError:
            print('Введите число!')
            continue

        match action:
            case 1:
                add_task()
            case 2:
                remove_task()
            case 3:
                change_task()
            case 4:
                list_task()
            case 5:
                list_tasks_category()
            case 6:
                search_tasks()
            case 7:
                break
            case _:
                print('Неверный ввод!')



if __name__ == "__main__":
    main()
