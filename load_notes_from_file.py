


# Создаём функцию для чтения файла и переноса содержимого в список словарей
def load_notes_from_file(filename):
    notes = []
    try:   # Открываем нужный файл с помощью конструкции with
        with open('filename.txt', 'r', encoding='utf-8') as filename:
            all_string = filename.readlines()
            if len(all_string) == 0:
                print('Открытый файл пуст')
                return notes

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
    except FileNotFoundError:
        print('Файл с таким именем не обнаружен. Создан новый файл')
        filename = open('filename.txt', 'x', encoding='utf-8')
        filename.close()
        return load_notes_from_file(filename='filename.txt')
    except UnicodeDecodeError:
        print('Ошибка при чтении файла filename. Проверьте его содержимое.')
    except PermissionError:
        print('Ошибка доступа')
    except Exception as e:
        print(f'Произошла ошибка {e}')

    # Проверяем результат
    print(notes)
    # Возвращаем из функции список словарей
    return notes

if __name__=='__main__':

    filename = load_notes_from_file(filename='filename.txt')