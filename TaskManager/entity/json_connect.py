import json
import os

'''Класс для работы с файлами json'''
class Connect:
    '''Функция для загрузки файла и получения/чтения информации'''
    @staticmethod
    def load(file: str) -> list:
        if not os.path.isfile(file):
            print(f'Файл {file} не найден')
            return []
        try:
            with open(file, 'r', encoding='utf-8') as db:
                content = db.read()
                return json.loads(content) if content.strip() else []
        except json.JSONDecodeError:
            print(f'Ошибка при чтении файла {file}')
            return []
        except Exception as e:
            print(f'Ошибка при загрузке {file}: {e}')
            return []

    '''Функция сохранения изменений в файл json'''
    @staticmethod
    def save(file: str,  tasks:list) -> None:
        try:
            with open(file, 'w', encoding='utf-8') as db:
                json.dump([task.__dict__ for task in tasks], db, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f'Ошибка при сохранении {file}: {e}')