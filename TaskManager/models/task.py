'''
Данный класс является моделью задач и имеет атрибуты:
task_id - является уникальным идентификатором задачи
title - название задачи
description - описание задачи
category - категория задачи
due_data - дата выполнения задачи
priority - приоритет задачи
status - статус задачи
'''

class Task:
    def __init__(self, task_id: int, title: str, description: str, category: str, due_date: str, priority: str,
                 status='Не выполнена'):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.category = category
        self.due_date = due_date
        self.priority = priority
        self.status = status

    def __str__(self):
        return f'ID: {self.task_id}, Название: {self.title}, Описание: {self.description}, Категория: {self.category}, Срок выполнения: {self.due_date}, Приоритет: {self.priority}, Статус: {self.status}'
