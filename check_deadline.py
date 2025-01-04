# Программа запускается и показывает текущую дату
from datetime import datetime
current_date = datetime.now().date()
print('Текущая дата: ', current_date.strftime('%d-%m-%Y'))
# Запрашиваем у пользователя дату дедлайна
# Переводим полученное значение в формат datetime для сравнения
while True:
    issue_date = input('Пожалуйста, введите дату истечения заметки\n'
      ' в формате "дд-мм-гггг"(через дефис и без пробелов): ')
    try:
        issue_date = datetime.strptime(issue_date, '%d-%m-%Y').date()
# Подтверждение правильного ввода
        print('Вы ввели: ', issue_date.strftime('%d-%m-%Y'))
# Проверяем правильность ввода
    except ValueError:
        print('Неверный ввод! Попробуйте ещё.')
        continue
# Сравниваем даты
    if issue_date == current_date:
        print('Внимание! Дедлайн истекает сегодня.')
        break
    if issue_date < current_date:
        difference = current_date - issue_date
        print('Внимание! Дедлайн истёк: ', difference.days, 'дней назад!')
        break
    if issue_date > current_date:
        difference_1 = issue_date - current_date
        print('Внимание! До дедлайна: ', difference_1.days, 'дней!')
        break
print('Конец')