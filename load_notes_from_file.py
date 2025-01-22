
# Создаём функцию для чтения файла и переноса содержимого в список словарей
def load_notes_from_file(filename):
    notes = []

    england_keys = {
        'Имя пользователя': 'username',
        'Заголовок': 'title',
        'Описание': 'content',
        'Статус': 'status',
        'Дата создания': 'created_date',
        'Дедлайн': 'issue_date'
    }
    try:   # Открываем нужный файл с помощью конструкции with
        with open(filename, 'r', encoding='utf-8') as file:
            all_string = file.read()
            if all_string:
                note_string = all_string.split('\n— — —\n')
                for string in note_string:
                    note_lines = string.split('\n')
                    note = {}
            # Назначаем ключ и значение с помощью разделения ":", записываем в словарь и добавляем в список
                    for line in note_lines:
                        russian_key, value = line.split(': ', 1)
                        key = england_keys[russian_key]
                        value = value.strip()
                        note[key] = value
                    notes.append(note)

    except FileNotFoundError:
        print('Файл с таким именем не обнаружен.')
    except UnicodeDecodeError:
        print('Ошибка при чтении файла filename. Проверьте его содержимое.')
    except PermissionError:
        print('Ошибка доступа')
    except Exception as e:
        print(f'Произошла ошибка: {e}')
    # Возвращаем из функции список словарей
    return notes

if __name__=='__main__':
    notes = load_notes_from_file(filename='filename.txt')
    print(notes)