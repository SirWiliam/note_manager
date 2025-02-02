# Загружаем библиотеку datetime для работы с датами
from datetime import datetime

# Создаём функцию создания заметки
def create_note():
# Просим пользователя ввести данные для заметки
    username = input('Введите ваше имя: ').strip()
    title = input('Введите заголовок заметки: ').strip()
    content = input('Введите описание заметки: ').strip()
    status = input('Введите статус заметки ("новая", "в процессе", "выполнена"): ').lower().strip()
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
        "username": username,
        "title": title,
        "content": content,
        "status": status,
        "created_date": created_date,
        "issue_date": datetime.strftime(issue_date, '%d-%m-%Y')
    }

    return note
if __name__ == '__main__':
    # Вызываем созданную функцию
    note = create_note()
    # Выводим результат работы функции на экран
    print("Заметка создана: ")
    print(*note.items(), sep='\n')