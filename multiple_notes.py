# Программа запускается с приветствия
from time import sleep

note_list = []
print('Добро пожаловать в менеджер заметок "Мысль"!')
while True:
    user_answer = input('Хотите добавить новую заметку? (да/нет): ')
    if user_answer == 'да':
        break
    if user_answer == 'нет':
        quit()
    else:
        print('Неверный ввод!')
        continue

i = 0
while True:
    print(f'Пожалуйста введите данные заметки №{i + 1}')
    i += 1
    titles = {}
    title = input('Введите заголовок вашей заметки: ')
    titles['Заголовок'] = title
    name = {}
    username = input('Введите ваше имя: ')
    name['Имя'] = username
    contents = {}
    content = input('Придумайте описание вашей заметки: ')
    contents['Описание'] = content
    statuses = {}
    status = input('Введите статус заметки (Например: "Выполняется" или Выполнена"): ')
    statuses['Статус заметки'] = status
    created_dates = {}
    created_date = input('Введите дату создания заметки в формате "дд-мм-гггг": ')
    created_dates['Дата создания'] = created_date
    issue_dates = {}
    issue_date = input('Введите дату дедлана заметки в формате "дд-мм-гггг": ')
    issue_dates['Дата дедлайна'] = issue_date
    print('Спасибо за ваши данные!')

    question = input('Хотите создать ещё одну заметку? (да/нет):')
    if question == 'да':
        continue
    else:
        print('Группируем ваши данные...')
        sleep(1)
        print('\n'.join())
        break