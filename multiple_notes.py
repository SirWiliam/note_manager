# Программа запускается с приветствия
from time import sleep
from datetime import datetime
note_list = []
print('Добро пожаловать в менеджер заметок "Мысль"!')
current_date = datetime.today().date()
print('Сегодня: ', current_date.strftime('%d-%m-%Y'))
while True:
    user_answer = input('Хотите добавить новую заметку? (да/нет): ').lower()
    if user_answer == 'да':
        break
    if user_answer == 'нет':
        quit('Конец работы программы!')
    else:
        print('Неверный ввод! Попробуйте ещё раз.')
        continue

i = 0
while True:
    print(f'Пожалуйста введите данные для заметки №{i + 1}')
    note = {}
    username = input('Введите ваше имя: ')
    note['Имя:'] = username
    if username == '':
        print('Неверный ввод!')
        continue
    title = input('Введите заголовок вашей заметки: ')
    note['Заголовок:'] = title
    if title == '':
        print('Неверный ввод!')
        continue
    elif title == note.values():
        print('Вы ввели похожий заголовок!')
        title_change = input('Хотите его заменить?(да/нет): ').lower()
        if title_change == 'да':
            continue
        elif title_change == 'нет':
            break
        else:
            print('Неверный ввод! Попробуйте ещё раз.')
            continue
    content = input('Придумайте описание вашей заметки: ')
    note['Описание:'] = content
    if content == '':
        print('Неверный ввод!')
        continue
    status = input('Введите статус заметки (Например: "Выполняется" или Выполнена"): ')
    note['Статус заметки:'] = status
    if status == '':
        print('Неверный ввод!')
        continue
    created_date = input('Введите дату создания заметки\n'
      'в формате "дд-мм-гггг"(через дефис и без пробелов): ')
    try:
        created_date = datetime.strptime(created_date, '%d-%m-%Y').date()
    except ValueError:
        print('Неверный ввод! Попробуйте ещё.')
        continue
    note['Дата создания:'] = created_date
    issue_date = input('Введите дату истечения заметки\n'
      ' в формате "дд-мм-гггг"(через дефис и без пробелов): ')
    try:
        issue_date = datetime.strptime(issue_date, '%d-%m-%Y').date()
    except ValueError:
        print('Неверный ввод! Попробуйте ещё.')
        continue
    if issue_date == current_date:
        print('Внимание! Дедлайн истекает сегодня.')
        break
    elif issue_date < current_date:
        difference = current_date - issue_date
        print('Внимание! Дедлайн истёк: ', difference.days, 'дней назад!')
        break
    elif issue_date > current_date:
        difference_1 = issue_date - current_date
        print('Внимание! До дедлайна: ', difference_1.days, 'дней!')
        break
    note['Дата дедлайна:'] = issue_date
    print('Спасибо за ваши данные!')
    note_list.append(note)
    i += 1
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
print('Вы создали следующие заметки: ')
a = 0
for item in note_list:
    print(f'Заметка №{a + 1}:')
    a += 1
    print(*item.items(), sep='\n')

print('Конец работы программы!')