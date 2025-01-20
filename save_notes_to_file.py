

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
# Функция принимает список заметок и записывает их в файл
def save_notes_to_file(notes, filename):

    # Открываем созданный файл в формате записи
    filename = open('filename.txt', 'w', encoding='utf-8')
    for item in notes:
        for key, value in item.items():
            filename.writelines(f'{key}: {value}\n')
        filename.write('— — —\n')

    # Закрываем файл после записи и возвращаем из функции
    filename.close()
    return filename

# Проверяем есть ли нужный нам файл
try:
    with open('filename.txt', 'w', encoding='utf-8') as filename:
        filename.close()
        # Передаём список в функцию и вызываем её
        notes = save_notes_to_file(notes, filename)
# Если файл отсутствует, выводится сообщение о создании нового
except FileNotFoundError:
    print('Файл с таким именем не обнаружен. Создан новый файл')
    filename = open('filename.txt', 'a+', encoding='utf-8')
    filename.close()
    # Передаём список в функцию и вызываем её
    notes = save_notes_to_file(notes, filename)
except UnicodeDecodeError:
    print('Ошибка при чтении файла filename. Проверьте его содержимое.')
except PermissionError:
    print('Ошибка доступа')

