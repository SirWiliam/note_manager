from time import sleep
from datetime import datetime
# Программа запускается и приветствует пользователя
note_list = []
print('Добро пожаловать в менеджер заметок "Мысль"!')
current_date = datetime.today().date()
print('Сегодня: ', current_date.strftime('%d-%m-%Y'))
# Программа предлагает создать заметку
while True:
    user_answer = input('Хотите добавить новую заметку? (да/нет): ').lower()
    if user_answer == 'да':
        break
    if user_answer == 'нет':
        quit('Конец работы программы!')
    else:
        print('Неверный ввод! Попробуйте ещё раз.')
        continue
# Если ответ положительный, начинается создание заметки
i = 0
while True:
    print(f'Пожалуйста введите данные для заметки №{i + 1}')
    note = {}
# Пользователь вводит своё имя
    while True:
        username = input('Введите ваше имя: ')
        note['Имя:'] = username
        if username == '':
            print('Неверный ввод! Попробуйте ещё раз')
            continue
        else:
            break
# Пользователь вводит заголовок заметки
    while True:
        title = input('Введите заголовок вашей заметки: ')
        note['Заголовок:'] = title
        if title == '':
            print('Неверный ввод! Попробуйте ещё раз.')
            continue
        else:
            break
# Пользователь вводит описание заметки
    while True:
        content = input('Придумайте описание вашей заметки: ')
        note['Описание:'] = content
        if content == '':
            print('Неверный ввод! Попробуйте ещё раз.')
            continue
        else:
            break
# Пользователь выбирает статус для своей заметки
    while True:
        status_list = {
            '1': "Выполняется",
            '2': "Выполнена",
            '3': "Отложена",
             }
        print('Выберите статус вашей заметки')
        print(*status_list.items(), sep='\n')
        status = input('Введите номер статуса который вам подходит: ')
        if status == '1':
            print('Ваш выбор: 1')
            print('Обновлённый статус заметки:', "Выполняется")
        elif status == '2':
            print('Ваш выбор: 2')
            print('Обновлённый статус заметки:', "Выполнена")
        elif status == '3':
            print('Ваш выбор: 3')
            print('Обновлённый статус заметки:', "Отложена")
        else:
            print('Не верный ввод! Попробуйте ещё раз.')
            continue
        update_status = input('Для изменения статуса введите любой символ\n'
                                  'или для отмены изменения нажмите - Enter: ')
        if update_status == type(str):
            continue
        elif update_status == '':
            note['Статус заметки:'] = status_list.get(status)
            break
# Пользователь вводит дату создания (не знаю зачем заставлять пользователя это делать)
    while True:
        created_date = input('Введите дату создания заметки\n'
                     'в формате "дд-мм-гггг"(через дефис и без пробелов): ')
        try:
            created_date = datetime.strptime(created_date, '%d-%m-%Y').date()
            note['Дата создания:'] = created_date.strftime('%d-%m-%Y')
            break
        except ValueError:
            print('Неверный ввод! Попробуйте ещё раз.')
            continue
# Пользователь вводит дату дедлайна заметки
    while True:
        issue_date = input('Введите дату истечения заметки\n'
                     'в формате "дд-мм-гггг"(через дефис и без пробелов): ')
        try:
            issue_date = datetime.strptime(issue_date, '%d-%m-%Y').date()
            note['Дата дедлайна:'] = issue_date.strftime('%d-%m-%Y')
        except ValueError:
            print('Неверный ввод! Попробуйте ещё раз.')
            continue
        if issue_date == created_date:
            print('Внимание! Дедлайн истекает сегодня.')
            break
        elif issue_date < created_date:
            difference = created_date - issue_date
            print('Внимание! Дедлайн истёк: ', difference.days, 'дней назад!')
            break
        elif issue_date > created_date:
            difference_1 = issue_date - created_date
            print('Внимание! До дедлайна: ', difference_1.days, 'дней!')
            break
# После всех действий заметка сохраняется в виде словаря в списке
    print('Создание заметки завершено.')
    note_list.append(note)
    i += 1
# Предлагается создать ещё одну заметку
    question = input('Хотите создать ещё одну заметку? (да/нет):').lower()
    if question == 'да':
        continue
    elif question == 'нет':
        print('Группируем ваши данные...')
        sleep(1)
        break
    else:
        print('Неверный ввод! Попробуйте ещё раз.')
        continue
# Выводится результат работы программы
print('Вы создали следующие заметки: ')
a = 0
for item in note_list:
    print(f'Заметка №{a + 1}:')
    a += 1
    print(*item.items(), sep='\n')