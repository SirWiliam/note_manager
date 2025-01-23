import json
# Создаём функцию для записи в формате .json
def save_notes_json(notes, filename):
    try:
        # Открываем\создаём файл для записи
        with open(filename, 'w', encoding='utf-8') as file:
            # Записываем с помощью метода json.dump
            json.dump(notes, file, indent=4, ensure_ascii=False)
    # Проверяем на ошибки
    except PermissionError:
        print('Ошибка: Недостаточно прав для записи в файл')
    except Exception as e:
        print(f'Произошла ошибка: {e}')

if __name__ == '__main__':
    # Список заметок который надо записать
    notes = [
        {
            'username': 'Алекс',
            'title': 'Список покупок',
            'content': 'Закупить продукты',
            'status': 'новая',
            'created_date': '20-01-2025',
            'issue_date': '30-01-2025'
        },
        {
            'username': 'Дима',
            'title': 'Спортзал',
            'content': 'Сходить в спортзал',
            'status': 'в процессе',
            'created_date': '20-01-2025',
            'issue_date': '01-02-2025'
        },
        {
            'username': 'Даша',
            'title': 'День рождения',
            'content': 'Купить подарок',
            'status': 'выполнено',
            'created_date': '20-03-2025',
            'issue_date': '26-05-2025'
        }
    ]

    save_notes_json(notes, filename='filename.json')