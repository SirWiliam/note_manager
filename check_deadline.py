# Программа запускается и показывает текущую дату
from calendar import month
from datetime import datetime

current_date = datetime.now().date()
print('Текущая дата: ', current_date.strftime('%d-%m-%Y'))
# Запрашиваем у пользователя дату дедлайна

issue_date = input('Пожалуйста, введите дату истечения заметки\n'
      ' в формате "дд-мм-гггг"(через дефис и без пробелов): ')

# Переводим полученное значение в формат datetime для сравнения
user_date = datetime.strptime(issue_date, '%d-%m-%Y').date()
print('Вы ввели: ', user_date.strftime('%d-%m-%Y'))
if issue_date == current_date.strftime('%d-%m-%Y'):
    print('Внимание! Дедлайн истекает сегодня.')
#if issue_date < current_date.strftime('%d-%m-%Y'):
    #if issue_date > current_datetime:
print('Конец')