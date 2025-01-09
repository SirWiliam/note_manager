# Загружаем библиотеку datetime для работы с датами
from datetime import datetime

# Создаём функцию создания заметки
def create_note():
# Просим пользователя ввести данные для заметки
    username = input('Введите ваше имя: ')
    title = input('Введите заголовок заметки: ')
    content = input('Введите описание заметки: ')
    status = input('Введите статус заметки (например, "новая", "в процессе", "выполнена"): ')
# Текущая дата вводится автоматически
    created_date = datetime.now().date().strftime('%d-%m-%Y')
# С помощью цикла вводим и проверяем правильность даты дедлайна
    while True:
        issue_date = input('Введите дату дедлайна заметки\n'
                    ' в формате "дд-мм-гггг"(через дефис и без пробелов): ')
        try:
            issue_date = datetime.strptime(issue_date, '%d-%m-%Y').date()
            break
        except ValueError:
            print('Неверный ввод! Попробуйте ещё.')
            continue
# Записываем все полученные данные в словарь
    note = {
        "Имя:": username,
        "Заголовок:": title,
        "Описание:": content,
        "Статус заметки:": status,
        "Дата создания:": created_date,
        "Дата дедлайна:": datetime.strftime(issue_date, '%d-%m-%Y')
    }

    return note

# Вызываем созданную функцию
note = create_note()
# Выводим результат работы функции на экран
print("Заметка создана: ", note)