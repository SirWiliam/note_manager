


notes = []
# Создаём функцию для чтения файла и переноса содержимого в список словарей
def load_notes_from_file(filename):

    # Открываем нужный файл с помощью функции with
    with open('filename.txt', 'r', encoding='utf-8') as file:
        all_string = file.readlines()
        if len(all_string) == 0:
            print('Открытый файл пуст')

        symbols = ('— — —\n')

        # Убираем ненужные символы за один проход
        all_string = [line for line in all_string if line != symbols]

        # Назначаем ключ и значение с помощью разделения ":", записываем в словарь и добавляем в список
        for i in all_string:
            note = {}
            key, value = i.split(':')
            value = value.strip()
            note[key] = value
            notes.append(note)

        # Проверяем результат
        print(notes)

        # Возвращаем из функции список словарей
        return notes

# Проверяем есть ли нужный нам файл
try:
    file = open('filename.txt', encoding='utf-8')
    file.close()
    # Вызываем функцию
    load_notes_from_file(file)
except FileNotFoundError:
    print('Файл с таким именем не обнаружен.')


