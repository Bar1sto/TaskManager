import os
import json
import pytest
from main import Task
from json_connect import Connect

TEST_FILE = "tasks.json"  # Временный файл для тестов


@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Создаем тестовый файл перед тестами
    with open(TEST_FILE, 'w') as file:
        json.dump([], file)
    yield
    # Удаляем тестовый файл после тестов
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)


def test_create_task():
    """Проверка создания новой задачи."""
    task = Task(1, 'Задача 1', 'Описание задачи', 'Работа', '2024-12-01', 'Средний')
    Task.add_task(task)
    tasks = Connect.load(TEST_FILE)

    assert len(tasks) == 1
    assert tasks[0]['name'] == 'Задача 1'
    assert tasks[0]['category'] == 'Работа'


def test_get_all_tasks():
    """Проверка получения всех задач."""
    tasks = [
        Task(1, 'Задача 1', 'Описание задачи', 'Работа', '2024-12-01', 'Средний').__dict__,
        Task(2, 'Задача 2', 'Описание задачи 2', 'Дом', '2024-12-02', 'Высокий').__dict__
    ]
    Connect.save(TEST_FILE, tasks)

    loaded_tasks = Task.list_task()

    assert len(loaded_tasks) == 2
    assert loaded_tasks[0]['id'] == 1
    assert loaded_tasks[1]['name'] == 'Задача 2'


def test_remove_task_by_id():
    """Проверка удаления задачи по ID."""
    tasks = [
        Task(1, 'Задача 1', 'Описание задачи', 'Работа', '2024-12-01', 'Средний').__dict__,
        Task(2, 'Задача 2', 'Описание задачи 2', 'Дом', '2024-12-02', 'Высокий').__dict__
    ]
    Connect.save(TEST_FILE, tasks)

    Task.remove_task(1)  # Удаляем задачу с ID = 1
    remaining_tasks = Connect.load(TEST_FILE)

    assert len(remaining_tasks) == 1
    assert remaining_tasks[0]['id'] == 2


def test_update_task_by_id():
    """Проверка обновления задачи по ID."""
    tasks = [
        Task(1, 'Задача 1', 'Описание задачи', 'Работа', '2024-12-01', 'Средний').__dict__
    ]
    Connect.save(TEST_FILE, tasks)

    Task.change_task(1, name='Обновленное имя', priority='Высокий')  # Обновляем задачу
    updated_tasks = Connect.load(TEST_FILE)

    assert len(updated_tasks) == 1
    assert updated_tasks[0]['name'] == 'Обновленное имя'
    assert updated_tasks[0]['priority'] == 'Высокий'


def test_filter_tasks_by_category():
    """Проверка фильтрации задач по категории."""
    tasks = [
        Task(1, 'Задача 1', 'Описание задачи', 'Работа', '2024-12-01', 'Средний').__dict__,
        Task(2, 'Задача 2', 'Описание задачи 2', 'Дом', '2024-12-02', 'Высокий').__dict__,
        Task(3, 'Задача 3', 'Описание задачи 3', 'Работа', '2024-12-03', 'Низкий').__dict__
    ]
    Connect.save(TEST_FILE, tasks)

    filtered_tasks = Task.list_tasks_category(category='Работа')

    assert len(filtered_tasks) == 2
    assert all(task['category'] == 'Работа' for task in filtered_tasks)
