from datetime import datetime
from colorama import init, deinit
from colorama import Fore, Style
init(autoreset=True)
notes = []
# Создаём функцию "Меню действий"
def menu():
    print(Fore.YELLOW +
        '    Меню действий:\n'
        '1. Создать новую заметку\n'
        '2. Показать все заметки\n'
        '3. Обновить заметку\n'
        '4. Удалить заметку\n'
        '5. Найти заметки\n'
        '6. Выйти из программы'
    )
    print('--------------------------------')
    while True:
        program_menu = input(Style.BRIGHT + 'Введите цифру действия которое хотите совершить: ')
        if program_menu == '1':
            print(Fore.YELLOW + 'Ваш выбор: 1. Создать новую заметку.')
            print('--------------------------------')
            create_note()
            break
        elif program_menu == '2':
            print(Fore.YELLOW + 'Ваш выбор: 2. Показать все заметки.')
            print('--------------------------------')
            display_notes(notes)
            break
        elif program_menu == '3':
            print(Fore.YELLOW + 'Ваш выбор: 3. Обновить заметку.')
            print('--------------------------------')
            update_note(notes)
            break
        elif program_menu == '4':
            print(Fore.YELLOW + 'Ваш выбор: 4. Удалить заметку.')
            print(Fore.RED + 'Извините, данная функция пока не реализована.')
            print('--------------------------------')
            return menu()
        elif program_menu == '5':
            print('Ваш выбор: 5. Найти заметки.')
            print('--------------------------------')
            search_notes(notes, keyword=None, status=None)
            break
        elif program_menu == '6':
            print('Завершение работы программы. Спасибо за использование!')
            quit()
        else:
            print('Неверный ввод. Пожалуйста попробуйте ещё раз.')
            continue

# Создаём функцию создания заметки
def create_note():
    print(Style.BRIGHT + 'Давайте создадим новую заметку!')
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
        "username": username,
        "title": title,
        "content": content,
        "status": status,
        "created_date": created_date,
        "issue_date": datetime.strftime(issue_date, '%d-%m-%Y')
    }
    notes.append(note)
# Выводим результат работы функции на экран
    print(Style.BRIGHT + "Заметка создана: ")
    print(*note.items(), sep='\n')
    print('--------------------------------')
    return notes and menu()



def display_notes(notes):
    print(Style.BRIGHT + 'Список ваших заметок:')
    if len(notes) == 0:
        print(Fore.RED + 'К сожалению у вас нет созданных заметок')
        print('--------------------------------')
        return menu()
    a = 0
    for item in notes:
        print('--------------------------------')
        print(Fore.CYAN, Style.BRIGHT + f'Заметка №{a + 1}:')
        a += 1
        print(*item.items(), sep='\n')
    return notes and menu()

def update_note(note):

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
    # Выбранные данные изменяются и записываются в словарь
    while True:
        if change == 'username':
            # Можно ввести любое имя, но поле не может быть пустым
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
            #Может быть введён любой заголовок, но моле не может быть пустым
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
                # Можно ввести любое описание, но поле не может быть пустым
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
                # Можно ввести любой статус, но поле не может быть пустым
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
    # Возвращаем обновлённую заметку
    return note and menu()


def search_notes(notes, keyword=None, status=None):
# Проверка для пустого списка
    if len(notes) == 0:
         print('Список заметок пуст.')
         return []

# Если не задано ключевое слово или статус вернуть исходный список заметок
    if keyword is None and status is None:
         return notes

    notes_list = []

    for note in notes:
        my_keyword = True
        my_status = True

# Поиск по ключевому слову
        if keyword is not None:
            keyword = keyword.lower()

# Поиск в имени пользователя, заголовке заметки или в описании заметки
            my_keyword = (
                    keyword in note['title'].lower() or
                    keyword in note['content'].lower() or
                    keyword in note['username'].lower()
            )

# Поиск по статусу
        if status is not None:
            my_status = note['status'].lower() == status.lower()

# Поиск по двум параметрам keyword и status
        if my_keyword and my_status:
            notes_list.append(note)

# Отобразить результат
    if len(notes_list) > 0:
        print('Результат поиска:')
        for i, note in enumerate(notes_list, 1):
            print(f'Заметка №{i}:')
            print(f'Имя пользователя: {note['username']}')
            print(f'Заголовок: {note['title']}')
            print(f'Описание: {note['content']}')
            print(f'Статус: {note['status']}')
            print(f'Дата создания: {note['created_date']}')
            print(f'Дата дедлайна: {note['issue_date']}')
            if i < len(notes_list):
                print('')
    else:
        print('Ваш запрос не дал результата.')
    return notes_list


menu()
deinit()