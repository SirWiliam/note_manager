
username = input('Пожалуйста, введите ваше имя (Пример: Иван): ')
title1 = input('Пожалуйста, придумайте заголовок первой заметки (Пример: Ужин): ')
title2 = input('Пожалуйста, придумайте заголовок второй заметки: ')
title3 = input('Пожалуйста, придумайте заголовок третьей заметки: ')
titles = [title1, title2, title3]
content = input('Пожалуйста, придумайте описание вашей заметки (Пример: Купить еду): ')
status = input('Пожалуйста, введите статус заметки (Пример: "Выполняется" или Выполнена"): ')
created_date = input('Пожалуйста, введите дату создания в формате "дд-мм-гггг": ')
issue_date = input('Пожалуйста, введите дату истечения заметки в формате "дд-мм-гггг": ')

print('\nВы ввели следующие данные:')
print('Имя пользователя:', username)
print('Заголовки ваших заметок:', titles)
print('Описание вашей заметки:', content)
print('Статус вашей заметки:', status)
print('Дата создания вашей заметки:', created_date)
print('Дата истечения вашей заметки:', issue_date)
