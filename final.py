
note = {}

note['username'] = input('Пожалуйста, введите ваше имя: ')
note['titles'] = []
for i in range (3):
    title = input(f'Пожалуйста, добавте заголовок заметки {i + 1}: ')
    note['titles'].append(title)
note['content'] = input('Пожалуйста, придумайте описание вашей заметки: ')
note['status'] = input('Пожалуйста, введите статус заметки (Например: "Выполняется" или Выполнена"): ')
note['created_date'] = input('Пожалуйста, введите дату создания в формате "дд-мм-гггг": ')
note['issue_date'] = input('Пожалуйста, введите дату истечения заметки в формате "дд-мм-гггг": ')

print('\nСобранная информация о заметке: ')
for key, value in note.items():
    print(f'{key.capitalize()}: {value}')

