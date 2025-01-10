# Загружаем библиотеку datetime для работы с датами
from datetime import datetime
# Создаём принимающую функцию
def update_note(note):
# Выводим заметку в удобном формате
    for key, value in note.items():
        print('{0}: {1}'.format(key, value))
print('Ваша заметка:')
note = {
    'username': 'Дима',
    'title': 'Спортзал',
    'content': 'Пойти в спортзал',
    'status': 'новая',
    'created_date': '28-11-2024',
    'issue_date': '3-02-2025'
}
update_note(note)
# Предлагаем пользователю выбрать данные для изменения
while True:
    print()
    change = input('Какие данные хотите обновить?\n'
        '("username, title, content, status, issue_date"): ')
    if (change == "username" or
        change == "title" or
        change ==  "content" or
        change == "status" or
        change == "issue_date"):
        break
    else:
        print('Неверный ввод! Попробуйте ещё раз пожалуйста.')
        continue

print()
# Выбранные данные изменяются и записываются в словарь
while True:
    if change == 'username':
        while True:
            username = input('Введите новое ваше имя: ')
            if username == '':
                print('Неверный ввод! Попробуйте ещё раз пожалуйста.')
                continue
            else:
                break
        note['username'] = username
        break
    elif change == 'title':
        while True:
            title = input('Введите новый заголовок заметки: ')
            if title == '':
                print('Неверный ввод! Попробуйте ещё раз пожалуйста.')
                continue
            else:
                break
        note['title'] = title
        break
    elif change == 'content':
        while True:
            content = input('Введите новое описание заметки: ')
            if content == '':
                print('Неверный ввод! Попробуйте ещё раз пожалуйста.')
                continue
            else:
                break
        note['content'] = content
        break
    elif change == 'status':
        while True:
            status = input('Введите  новый статус заметки (например, "новая", "в процессе", "выполнена"): ')
            if status == '':
                print('Неверный ввод! Попробуйте ещё раз пожалуйста.')
                continue
            else:
                break
        note['status'] = status
        break
    elif change == 'issue_date':
        while True:
            issue_date = input('Введите новую дату дедлайна заметки\n'
                    ' в формате "дд-мм-гггг"(через дефис и без пробелов): ')
            try:
                issue_date = datetime.strptime(issue_date, '%d-%m-%Y').date()
                break
            except ValueError:
                print('Неверный ввод! Попробуйте ещё.')
                continue
        note['issue_date'] = datetime.strftime(issue_date, '%d-%m-%Y')
        break

# Выводим результат работы программы
print('--------------------------')
print('Ваша обновлённая заметка:')
print()
update_note(note)
