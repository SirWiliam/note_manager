# Создаём файл в который будем записывать заметки
filename = open('filename.txt', 'w', encoding='utf-8')
filename.close()

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

# Функция которая принимает список заметок и записывает их в файл
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

# Передаём список в функцию и вызываем её
notes = save_notes_to_file(notes, filename)
