import pytest
from entity.json_connect import Connect
from models.task import Task

TEST_FILE = 'test_task.json'


@pytest.fixture(autouse=True)
def clear_test_file():
    """Фикстура для очистки тестового файла перед каждым тестом."""
    Connect.save(TEST_FILE, [])
    yield
    Connect.save(TEST_FILE, [])


def test_add_task(monkeypatch):
    """Тест добавления задачи."""
    inputs = iter(['Сходить в институт', 'Проснуться и пойти в институт на 1 пару', 'Учеба', '2024-12-01', 'Высокий'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr('main.Task.add_task', lambda: None)  # Убираем ввод

    Task.add_task()
    tasks = Connect.load(TEST_FILE)

    assert len(tasks) == 1
    assert tasks[0]['title'] == 'Сходить в институт'
    assert tasks[0]['description'] == 'Проснуться и пойти в институт на 1 пару'


def test_list_task():
    """Тест вывода списка задач."""
    tasks = [
        Task(1, 'Купить продукты', 'Список покупок', 'Дом', '2024-12-05', 'Средний').__dict__,
        Task(2, 'Завершить проект', 'Финальная презентация', 'Работа', '2024-12-10', 'Высокий').__dict__
    ]
    Connect.save(TEST_FILE, tasks)

    listed_tasks = Connect.load(TEST_FILE)

    assert len(listed_tasks) == 2
    assert listed_tasks[0]['category'] == 'Дом'
    assert listed_tasks[1]['category'] == 'Работа'


def test_remove_task(monkeypatch):
    """Тест удаления задачи по ID."""
    tasks = [
        Task(1, 'Купить продукты', 'Список покупок', 'Дом', '2024-12-05', 'Средний').__dict__,
        Task(2, 'Завершить проект', 'Финальная презентация', 'Работа', '2024-12-10', 'Высокий').__dict__
    ]
    Connect.save(TEST_FILE, tasks)

    monkeypatch.setattr('builtins.input', lambda _: '1')
    Task.remove_task()

    remaining_tasks = Connect.load(TEST_FILE)

    assert len(remaining_tasks) == 1
    assert remaining_tasks[0]['task_id'] == 2
