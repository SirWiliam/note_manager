
username = input('Пожалуйста, введите ваше имя: ')
title = input('Пожалуйста, введите название вашей заметки: ')
content = input('Пожалуйста, придумайте описание вашей заметки: ')
status = input('Пожалуйста, введите статус заметки (Например: "Выполняется" или Выполнена"): ')
created_date = input('Пожалуйста, введите дату создания в формате "дд-мм-гггг": ')
issue_date = input('Пожалуйста, введите дату истечения заметки в формате "дд-мм-гггг": ')

temp_created_date = created_date[0:5]
temp_issue_date = issue_date[0:5]

print('\nВы ввели следующие данные: ')
print('Имя пользователя: ', username)
print('Название заметки: ', title)
print('Описание вашей заметки: ', content)
print('Статус вашей заметки: ', status)
print('Дата создания: ', temp_created_date)
print('Дата истечения: ', temp_issue_date)
