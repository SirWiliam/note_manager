

# Функция принимает список заметок и записывает их в файл
def save_notes_to_file(notes, filename):
    try:
        with open('filename.txt', 'w', encoding='utf-8') as filename:
            for note in notes:
                filename.write(f'Имя пользователя: {note['username']}\n')
                filename.write(f'Заголовок: {note['title']}\n')
                filename.write(f'Описание: {note['content']}\n')
                filename.write(f'Статус: {note['status']}\n')
                filename.write(f'Дата создания: {note['created_date']}\n')
                filename.write(f'Дедлайн: {note['issue_date']}\n')
                filename.write('— — —\n')
    except PermissionError:
        print('Ошибка доступа')
    except Exception as e:
        print(f'Произошла ошибка {e}')
    return notes

if __name__=='__main__':
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
    notes = save_notes_to_file(notes, filename='filename.txt')








