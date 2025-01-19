

file = open('filename.txt', encoding='utf-8')
file.close()
notes = []
# Создаём функцию для чтения файла и переноса содержимого в список словарей
def load_notes_from_file(filename):

    # Открываем нужный файл с помощью функции with
    with open('filename.txt', 'r', encoding='utf-8') as file:
        all_string = file.readlines()
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

        # Возвращаем из функции список словарей
        return notes

# Вызываем функцию
load_notes_from_file(file)

# Проверяем результат
print(notes)