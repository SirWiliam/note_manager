# Создаём список для заголовков
titles = []

# Создаём бесконечный цикл для ввода заголовков
while True:
    title = input('Пожалуйста, добавте заголовок заметки\n'
                  ' (Enter для отмены): ').capitalize()

# Создаём условия для остановки создания новых заголовков
    if title == '':
        break
    titles.append(title)
# Проверяем каждый ввод
    print('Вы ввели:', title)

# Выводим итог работы программы
print("Ваши заголовки: ")
print('\n'.join(titles))