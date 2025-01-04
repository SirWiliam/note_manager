# Создаём словарь со статусами заметок
status_list = {'1': "Выполняется",
               '2': "Выполнена",
               '3': "Отложена",
               '4': "Просрочена"}
# Начало работы программы
print('Статус вашей заметки: ', 'Выполняется')

# Запрашиваем ввод статуса текущей заметки
while True:
    print('Пожалуйста, выберите новый статус вашей заметки')
    print(*status_list.items(), sep='\n')
    status = input('Введите номер статуса который вам подходит: ')
    if status == '1':
        print('Ваш выбор: 1')
        print('Обновлённый статус заметки:', "Выполняется")
        update_status = input('Для изменения статуса введите - "Поменять"\n'
                          'Для отмены изменения нажмите - Enter: ')
        if update_status == 'Поменять':
            continue
        elif update_status == '':
            break
    if status == '2':
        print('Ваш выбор: 2')
        print('Обновлённый статус заметки:', "Выполнена")
        update_status = input('Для изменения статуса введите - "Поменять"\n'
                            'Для отмены изменения нажмите - Enter: ')
        if update_status == 'Поменять':
          continue
        elif update_status == '':
          break
    if status == '3':
        print('Ваш выбор: 3')
        print('Обновлённый статус заметки:', "Отложена")
        update_status = input('Для изменения статуса введите - "Поменять"\n'
                            'Для отмены изменения нажмите - Enter: ')
        if update_status == 'Поменять':
            continue
        elif update_status == '':
            break
    if status == '4':
        print('Ваш выбор: 4')
        print('Обновлённый статус заметки:', "Просрочена")
        update_status = input('Для изменения статуса введите - "Поменять"\n'
                            'Для отмены изменения нажмите - Enter: ')
        if update_status == 'Поменять':
            continue
        elif update_status == '':
            break
    else:
        print('Не верный ввод!')
        continue

# Предлагаем пользователю изменить статус
print('Статус вашей заметки: ', status_list.get(status))

